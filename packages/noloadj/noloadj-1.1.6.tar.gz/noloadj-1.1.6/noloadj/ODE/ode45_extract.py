import jax.numpy as np
from jax.lax import *
from jax import custom_jvp,jvp
from functools import partial
import types

def odeint45_extract(f,y0,*args,h0=1e-5,stop=None,constraints=None,
                     param_T=(0.,0.),event=[],tol=1.48e-8):
    return _odeint45(f,event,h0,stop,constraints,param_T,tol,y0,*args)

def rk_step(y_prev, t_prev, h,f,*args):
    temp=f(y_prev, t_prev,*args)
    k1 = temp
    k2 = f(y_prev + h*0.2 * k1, t_prev + 0.2 * h,*args)
    k3 = f(y_prev + h*(3 * k1 + 9 * k2) / 40, t_prev + 3 * h / 10,*args)
    k4 = f(y_prev + h*(44 * k1 / 45 - 56 * k2 / 15 + 32 * k3 / 9),t_prev +
           4 * h / 5,*args)
    k5 = f(y_prev + h*(19372 * k1 / 6561 - 25360 * k2 / 2187 + 64448 * k3 / 6561
                       - 212 * k4 / 729),t_prev + 8 * h / 9,*args)
    k6 = f(y_prev + h*(9017 * k1 / 3168 - 355 * k2 / 33 + 46732 * k3 / 5247 +
                       49 * k4 / 176 - 5103 * k5 / 18656),t_prev + h,*args)
    k7 = f(y_prev + h*(35 * k1 / 384 + 500 * k3 / 1113 + 125 * k4 / 192 -
                       2187 * k5 / 6784 + 11 * k6 / 84),t_prev + h,*args)

    y = y_prev + h *(35 * k1 / 384 + 500 * k3 / 1113 + 125 * k4 / 192 -
                     2187 * k5 / 6784 + 11 * k6 / 84)
    yest = y_prev + h *(5179 * k1 / 57600 + 7571* k3 / 16695 + 393 * k4 / 640
                        - 92097 * k5 / 339200 + 187 * k6 / 2100 + k7 / 40)

    for j in range(len(y)):
        yj,yjest=cond(temp[j]!=False,lambda state:state,lambda state:(y_prev[j],
                                                    y_prev[j]),(y[j],yest[j]))
        y=y.at[j].set(yj)
        yest=yest.at[j].set(yjest)
    t_now = t_prev + h
    return y, yest, t_now


def optimal_step(y,yest,h,tol,errcon=1.89e-4):
    est=np.linalg.norm(y - yest)
    R = (est+1e-16) / h
    err_ratio = R / tol
    delta = (2*err_ratio)**(-0.2)
    h =np.where(est>=errcon,h*delta,1.0*h)
    return h

def envoyer_pdi(t,duree,periode):
    tpdi= cond(t-(t//periode)*periode<duree,lambda t:duree+(t//periode)*periode,
               lambda t:((t//periode)+1)*periode,t)
    return tpdi

def interpolation(state):
    y,h,y_prev,t_prev,t_now,output,outputprev=state
    tchoc=(-t_prev*output+t_now*outputprev)/(outputprev-output)
    h=tchoc-t_prev
    ychoc=(y_prev-y)*tchoc/(t_prev-t_now)+(t_prev*y-t_now*y_prev)/(t_prev-t_now)
    return ychoc,h,y_prev,t_prev,tchoc,output,outputprev

def prediction(t,tprev,val_seuil,output,outputprev):
    return t+(t-tprev)*(val_seuil-output)/(output-outputprev)

def GetTimeofNextVarHit(t,tprev,output,outputprev,seuil,duree,periode):
    tevent=envoyer_pdi(t,duree,periode)
    for i in range(len(output)):
        temp=prediction(t,tprev,seuil[i],output[i],outputprev[i])
        tevent=cond(temp>t,lambda tevent:np.minimum(tevent,temp),
                    lambda tevent:tevent,tevent)
    return tevent+1e-12

@partial(custom_jvp,nondiff_argnums=(0,1,2,3,4,5,6))
def _odeint45(f,event,h0,stop,constraints,param_T,tol,y0,*args):

    def cond_fn(state):
        y_prev2,_,y_prev,t_prev,h,cstr,_=state
        type,cond_stop=stop
        if type=='seuil':
            val,seuil=cond_stop(y_prev)
            valp,_=cond_stop(y_prev2)
            return (h>0) & (np.sign(val-seuil)==np.sign(valp-seuil))
        else:
            return (h > 0) & cond_stop(t_prev,t_prev+h,cstr,h)

    def body_fn(state):
        _,_,y_prev,t_prev,h,cstr,i=state
        y,yest,t_now,inew,hopt,condition=None,None,0.,0,0.,None
        if isinstance(f, types.FunctionType):
            y,yest,t_now=rk_step(y_prev,t_prev,h,f,*args)
            inew=i
            if event!=[]:
                for e in event:
                    valeur,chgt_etat=e
                    output,signe,seuil=valeur(y)
                    outputprev,_,_=valeur(y_prev)
                    if signe=='inf':
                        condition=np.bitwise_and(output<seuil,
                           np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                    elif signe=='sup':
                        condition=np.bitwise_and(output>seuil,
                            np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                    hopt = optimal_step(y, yest, h, tol)
                    y,h,_,_,t_now,_,_=cond(condition,interpolation,
                            lambda state:state,
                        (y,h,y_prev,t_prev,t_now,output-seuil,outputprev-seuil))
                    y=np.where(condition,chgt_etat(y),y)
            elif event==[]:
                hopt = optimal_step(y, yest, h, tol)
        elif not isinstance(f, types.FunctionType):
            f.etat=i
            y,yest,t_now=rk_step(y_prev,t_prev,h,f.derivative,*args)
            inew,y=f.event(y, t_now,i)
            output,seuil=f.output(y)
            outputprev,_=f.output(y_prev)
            tevent=GetTimeofNextVarHit(t_now,t_prev,output,outputprev,seuil,
                                       coeff*periode,periode)
            hopt = optimal_step(y,yest, h, tol)
            hopt=np.minimum(tevent-t_now,hopt)
            hopt=np.where(inew!=i,h0,hopt) # pour accelerer execution

        type,cond_stop=stop
        if type=='seuil':
            output,seuil=cond_stop(y)
            outputprev,_=cond_stop(y_prev)
            y,hopt,_,_,t_now,_,_=cond(
                np.sign(output-seuil)!=np.sign(outputprev-seuil),interpolation,
                lambda state:state,(y,hopt,y_prev,t_prev,t_now,output-seuil,
                                    outputprev-seuil))

        if constraints is not None:
            for i in range(len(constraints)):
                if isinstance(constraints[i][1],tuple):
                    test_exp,(expression,_)=constraints[i]
                else:
                    (expression,_)=constraints[i]
                if len(constraints)==1:
                    cstr=expression(t_prev,y_prev,t_now,y,cstr,h,periode)
                else:
                    if isinstance(constraints[i][1],tuple):
                        temp = cond(test_exp(t_now),lambda cstri:
                          expression(t_prev, y_prev, t_now, y, cstri,h,periode),
                                    lambda cstri: cstri, cstr[i])
                    else:
                        temp = expression(t_prev, y_prev,
                                          t_now, y, cstr[i],h,periode)
                    cstr=cstr.at[i].set(temp)

        return y_prev,t_prev,y,t_now,hopt,cstr,inew

    cstr=[]                 # INITIALISATION
    coeff, periode = param_T
    if constraints is not None:
        if len(constraints)==1:
            cstr=0.
        else:
            cstr=np.zeros(len(constraints))
        for i in range(len(constraints)):
            if isinstance(constraints[i][1],tuple):
                test_exp,(expression,_)=constraints[i]
            else:
                (expression,_)=constraints[i]
            if len(constraints)==1:
                cstr=expression(-h0, np.zeros(len(y0)), 0., y0, cstr,h0,periode)
            else:
                if isinstance(constraints[i][1],tuple):
                    temp = cond(test_exp(0.),lambda cstri: expression(-h0,
                        np.zeros(len(y0)), 0., y0, cstri,h0,periode),
                                lambda cstri: cstri, cstr[i])
                else:
                    temp=expression(-h0, np.zeros(len(y0)), 0., y0, cstr[i],
                                    h0,periode)
                cstr=cstr.at[i].set(temp)
    _,_,yf,tchoc,h,cstr,_ = while_loop(cond_fn, body_fn, (y0,0.,y0,0.,h0,cstr,0))
    return (tchoc,yf,cstr)


@_odeint45.defjvp
def _odeint45_jvp(f,event,h0,stop,constraints,param_T,tol, primals, tangents):
  y0,  *args = primals
  delta_y0,  *delta_args = tangents
  nargs = len(args)

  def f_aug(y0,delta_y0, t, *args_and_delta_args):
    args, delta_args = args_and_delta_args[:nargs], args_and_delta_args[nargs:]
    tangent_dot=None
    if isinstance(f, types.FunctionType):
        primal_dot, tangent_dot = jvp(f, (y0, t, *args), (delta_y0, 0.,
                                                          *delta_args))
    elif not isinstance(f, types.FunctionType):
        primal_dot, tangent_dot = jvp(f.derivative, (y0, t, *args), (delta_y0,
                                                            0., *delta_args))
    return tangent_dot

  yf,cstr,tchoc,yf_dot,cstr_dot = odeint45_etendu(f,f_aug,nargs,event,h0,stop,
                    constraints,param_T,tol, y0,delta_y0, *args, *delta_args)
  return (tchoc,yf,cstr),(tchoc,yf_dot,cstr_dot)


def rk_step_der(y_prev, t_prev, delta_y_prev,h,f,f_aug,nargs,*args):
    temp = f(y_prev,t_prev, *args[:nargs])
    k1 = f_aug(y_prev, delta_y_prev, t_prev, *args)
    k2 = f_aug(y_prev, delta_y_prev + h * 0.2 * k1, t_prev + 0.2 * h, *args)
    k3 = f_aug(y_prev, delta_y_prev + h * (3 * k1 + 9 * k2) / 40,t_prev +
               3 * h / 10, *args)
    k4 = f_aug(y_prev, delta_y_prev + h * (44 * k1 / 45 - 56 * k2 / 15 +
                                        32 * k3 / 9), t_prev + 4 * h / 5,*args)
    k5 = f_aug(y_prev, delta_y_prev + h * (19372 * k1 / 6561 - 25360 * k2 / 2187
            + 64448 * k3 / 6561 - 212 * k4 / 729),t_prev + 8 * h / 9, *args)
    k6 = f_aug(y_prev, delta_y_prev + h * (9017 * k1 / 3168 - 355 * k2 / 33 +
       46732 * k3 / 5247 + 49 * k4 / 176 - 5103 * k5 / 18656),t_prev + h, *args)
    delta_y = delta_y_prev + h *(35 * k1 / 384 + 500 * k3 / 1113 +
                        125 * k4 / 192 - 2187 * k5 / 6784 + 11 * k6 / 84)
    for j in range(len(delta_y)):
        delta_yj=cond(temp[j]!=False,lambda state:state,lambda state:
                        delta_y_prev[j],delta_y[j])
        delta_y=delta_y.at[j].set(delta_yj)
    return delta_y


def odeint45_etendu(f,f_aug,nargs,event,h0,stop,constraints,param_T,tol,y0,
                    delta_y0,*args):
    args_red = args[:nargs]

    def cond_fn(state):
        y_prev2,_,_,y_prev,delta_y_prev, t_prev, h,cstr,_,_ = state
        type,cond_stop=stop
        if type=='seuil':
            val,seuil=cond_stop(y_prev)
            valp,_ = cond_stop(y_prev2)
            return (h>0) & (np.sign(val-seuil)==np.sign(valp-seuil))
        else:
            return (h > 0) & cond_stop(t_prev,t_prev+h,cstr,h)

    def body_fn(state):
        _,_,_,y_prev,delta_y_prev, t_prev, h,cstr,delta_cstr,i = state
        y,yest,delta_y,t_now,inew,hopt,condition = None, None, None,0.,None,0.,\
                                                   None
        if isinstance(f, types.FunctionType):
            y,yest,t_now=rk_step(y_prev,t_prev,h,f,*args_red)
            inew=i
            if event!=[]:
                for e in event:
                    valeur,chgt_etat=e
                    output,signe,seuil=valeur(y)
                    outputprev,_,_=valeur(y_prev)
                    if signe=='inf':
                        condition=np.bitwise_and(output<seuil,
                            np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                    elif signe=='sup':
                        condition=np.bitwise_and(output>seuil,
                            np.bitwise_not(np.allclose(outputprev-seuil,0.)))
                    hopt = optimal_step(y, yest, h, tol)
                    y,h,_,_,t_now,_,_=cond(condition,interpolation,
                                           lambda state:state,
                        (y,h,y_prev,t_prev,t_now,output-seuil,outputprev-seuil))
                    y=np.where(condition,chgt_etat(y),y)
            elif event==[]:
                hopt = optimal_step(y, yest, h, tol)
        elif not isinstance(f, types.FunctionType):
            f.etat=i
            y,yest,t_now=rk_step(y_prev,t_prev,h,f.derivative,*args_red)
            inew,y=f.event(y, t_now,i)
            output,seuil=f.output(y)
            outputprev,_=f.output(y_prev)
            tevent=GetTimeofNextVarHit(t_now,t_prev,output,outputprev,seuil,
                                       coeff*periode,periode)
            hopt = optimal_step(y,yest, h, tol)
            hopt=np.minimum(tevent-t_now,hopt)
            hopt=np.where(inew!=i,h0,hopt)

        type,cond_stop=stop
        if type=='seuil':
            output,seuil=cond_stop(y)
            outputprev,_=cond_stop(y_prev)
            y,hopt,_,_,t_now,_,_=cond(
                np.sign(output-seuil)!=np.sign(outputprev-seuil),interpolation,
                        lambda state:state,(y,hopt,y_prev,t_prev,t_now,
                                            output-seuil,outputprev-seuil))

        if isinstance(f, types.FunctionType):
            delta_y = rk_step_der(y_prev, t_prev, delta_y_prev, h, f, f_aug,
                                  nargs, *args)
        elif not isinstance(f, types.FunctionType):
            delta_y = rk_step_der(y_prev, t_prev, delta_y_prev, h, f.derivative,
                                  f_aug, nargs, *args)

        if constraints is not None:
            for i in range(len(constraints)):
                if isinstance(constraints[i][1], tuple):
                    test_exp,(expression,der_expression) = constraints[i]
                else:
                    (expression,der_expression)=constraints[i]
                if len(constraints) == 1:
                    cstr = expression(t_prev, y_prev, t_now,y, cstr,h,periode)
                    delta_cstr=der_expression(t_prev, y_prev,delta_y_prev, t_now,
                                        y,delta_y,cstr, delta_cstr,h,periode)
                else:
                    if isinstance(constraints[i][1], tuple):
                        temp = cond(test_exp(t_now),lambda cstri:
                          expression(t_prev, y_prev, t_now,y, cstri,h,periode),
                                    lambda cstri: cstri, cstr[i])
                        delta_temp = cond(test_exp(t_now),lambda delta_cstri:
                           der_expression(t_prev, y_prev,delta_y_prev, t_now, y,
                                    delta_y,cstr[i], delta_cstri,h,periode),
                                lambda delta_cstri: delta_cstri, delta_cstr[i])
                    else:
                        temp = expression(t_prev, y_prev, t_now,y, cstr[i],h,
                                          periode)
                        delta_temp=der_expression(t_prev, y_prev,delta_y_prev,
                            t_now, y,delta_y,cstr[i], delta_cstr[i],h,periode)
                    cstr = cstr.at[i].set(temp)
                    delta_cstr = delta_cstr.at[i].set(delta_temp)
        return y_prev,delta_y_prev,t_prev,y, delta_y,t_now, hopt,cstr,\
               delta_cstr,inew

    cstr,delta_cstr = [],[]         # INITIALISATION
    coeff, periode = param_T
    if constraints is not None:
        if len(constraints) == 1:
            cstr = 0.
            delta_cstr=0.
        else:
            cstr = np.zeros(len(constraints))
            delta_cstr= np.zeros(len(constraints))
        for i in range(len(constraints)):
            if isinstance(constraints[i][1], tuple):
                test_exp,(expression,der_expression) = constraints[i]
            else:
                (expression, der_expression) = constraints[i]
            if len(constraints) == 1:
                cstr = expression(-h0, np.zeros(len(y0)), 0.,y0, cstr,h0,periode)
                delta_cstr=der_expression(-h0, np.zeros(len(y0)),
                   np.zeros(len(delta_y0)), 0., y0,delta_y0,cstr, delta_cstr,
                                          h0,periode)
            else:
                if isinstance(constraints[i][1], tuple):
                    temp = cond(test_exp(0.),lambda cstri: expression(-h0,
                       np.zeros(len(y0)), 0.,y0, cstri,h0,periode),
                                lambda cstri: cstri, cstr[i])
                    delta_temp = cond(test_exp(0.),lambda delta_cstri:
                      der_expression(-h0, np.zeros(len(y0)),
                        np.zeros(len(delta_y0)), 0., y0,delta_y0,cstr[i],
                        delta_cstri,h0,periode),lambda delta_cstri: delta_cstri,
                                      delta_cstr[i])
                else:
                    temp=expression(-h0, np.zeros(len(y0)), 0.,y0, cstr[i],h0,
                                    periode)
                    delta_temp=der_expression(-h0, np.zeros(len(y0)),
                        np.zeros(len(delta_y0)), 0., y0,delta_y0,cstr[i],
                                              delta_cstr[i],h0,periode)
                cstr = cstr.at[i].set(temp)
                delta_cstr = delta_cstr.at[i].set(delta_temp)

    _,_,_,yf,delta_yf,ts, h ,cstr1,delta_cstr1,_ = while_loop(cond_fn, body_fn,
                    (y0,delta_y0,0.,y0,delta_y0,0.,h0,cstr,delta_cstr,0))
    return yf,cstr1,ts,delta_yf,delta_cstr1


def T_pair(T):
    return lambda t:(t//T)%2==0

def T_impair(T):
    return lambda t:(t//T)%2!=0

def T_numero(T,n,i):
    return lambda t:(t//T)%n!=i

def Min(ind):
    return lambda t_prev,y_prev,t,y,cstr,h,_:np.minimum(y[ind],cstr),\
           lambda t_prev,y_prev,dprev,t,y,dy,cstr,dcstr,h,_:\
               np.where(np.minimum(cstr,y[ind])==y[ind],dy[ind],dcstr)

def Max(ind):
    return lambda t_prev,y_prev,t,y,cstr,h,_:np.maximum(y[ind],cstr),\
           lambda t_prev,y_prev,dprev,t,y,dy,cstr,dcstr,h,_:\
               np.where(np.maximum(cstr,y[ind])==y[ind],dy[ind],dcstr)


def min_T(T,ind):
    return lambda t_prev,y_prev,t,y,cstr,h,_:cond((t_prev//T)==(t//T),
            lambda cstr:np.minimum(y[ind],cstr),lambda cstr:y[ind],cstr),\
           lambda t_prev,y_prev,dprev,t,y,dy,cstr,dcstr,h,_:\
            cond((t_prev//T)==(t//T),lambda dcstr:np.where(np.minimum(cstr,
                y[ind])==y[ind],dy[ind],dcstr),lambda dcstr:dy[ind],dcstr)

def max_T(T,ind):
    return lambda t_prev,y_prev,t,y,cstr,h,_:cond((t_prev//T)==(t//T),
            lambda cstr:np.maximum(y[ind],cstr),lambda cstr:y[ind],cstr),\
           lambda t_prev,y_prev,dprev,t,y,dy,cstr,dcstr,h,_:\
            cond((t_prev//T)==(t//T),lambda dcstr:np.where(np.maximum(cstr,
                y[ind])==y[ind],dy[ind],dcstr),lambda dcstr:dy[ind],dcstr)

def moy_T(ind):
    return lambda t_prev,y_prev,t,y,cstr,h,T: cond((t_prev // T) == (t // T),
        lambda cstr: cstr+0.5*h*(y_prev[ind]+y[ind])/T,lambda cstr: 0., cstr),\
        lambda t_prev, y_prev, dprev, t, y, dy,cstr, dcstr, h,T: \
        cond((t_prev // T) == (t // T),lambda dcstr: dcstr+0.5*h*(dprev[ind]+
                                        dy[ind])/T,lambda dcstr: 0., dcstr)

def eff2_T(ind): # valeur efficace au carre
    return lambda t_prev, y_prev, t, y, cstr,h,T: cond((t_prev//T)==(t//T),
        lambda cstr: cstr+0.5*h*(y_prev[ind]**2+y[ind]**2)/T,lambda cstr: 0.,
        cstr),lambda t_prev, y_prev, dprev,t, y, dy,cstr,dcstr,h,T: \
        cond((t_prev//T)==(t//T),lambda dcstr: dcstr+0.5*h*(2*y_prev[ind]*
                dprev[ind]+2*y[ind]*dy[ind])/T,lambda dcstr: 0., dcstr)

def reg_perm(T,nb,nb_var,a=1e-5):
    constr = []
    for i in range(nb_var):
        constr.append((T_pair(nb * T), min_T(nb * T, i)))
        constr.append((T_impair(nb * T), min_T(nb * T, i)))
        constr.append((T_pair(nb * T), max_T(nb * T, i)))
        constr.append((T_impair(nb * T), max_T(nb * T, i)))
    def regime_perm(t_prev,t,cstr,h):
        vectp,vectimp=np.zeros(2*nb_var),np.zeros(2*nb_var)
        for i in range(nb_var):
            vectp=vectp.at[i].set(cstr[2*i])
            vectp=vectp.at[2*i+1].set(cstr[2*(2*i+1)])
            vectimp=vectimp.at[i].set(cstr[2*i+1])
            vectimp=vectimp.at[2*i+1].set(cstr[2*(2*i+1)+1])
        return np.bitwise_not(np.bitwise_and(np.allclose(vectp,vectimp,atol=a),
                                             np.not_equal(t_prev//T,t//T)))
    return ('rp',regime_perm),constr

