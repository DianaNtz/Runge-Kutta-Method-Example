"""
The code below was written by @author: https://github.com/DianaNtz and is an 
implementation of the second, third and fourth order Runge Kutta algorithm. 
It solves the differential equation u'=-(t-a)u.
"""
import numpy as np
import matplotlib.pyplot as plt
#some initial values
t0=0
tfinal=10
dt=0.12
steps=int((tfinal-t0)/dt)
u0=0.0000001
a=6
#differential equation function f
def f(t,u):
    return -(t-a)*u
t=np.empty(steps+1, dtype='double')
tn=t0
u2=np.empty(steps+1, dtype='double')
un2=u0
u3=np.empty(steps+1, dtype='double')
un3=u0
u4=np.empty(steps+1, dtype='double')
un4=u0
for i in range(0,steps+1):    
    t[i]=tn
    #Runge Kutta second
    u2[i]=un2
    k1=dt*f(tn,un2)
    k2=dt*f(tn+0.5*dt,un2+0.5*k1)
    un2=un2+k2
    #Runge Kutta third
    u3[i]=un3
    k1=dt*f(tn,un3)
    k2=dt*f(tn+0.5*dt,un3+0.5*k1)
    k3=dt*f(tn+dt,un3-k1+2*k2)
    un3=un3+k2*(4/6)+k1*(1/6)+k3*(1/6)
    #Runge Kutta fourth
    u4[i]=un4
    k1=dt*f(tn,un4)
    k2=dt*f(tn+0.5*dt,un4+0.5*k1)
    k3=dt*f(tn+0.5*dt,un4+0.5*k2)
    k4=dt*f(tn+dt,un4+k3)
    un4=un4+k2*(2/6)+k1*(1/6)+k3*(2/6)+k4*(1/6)
    tn=tn+dt
#analytical solution
ua=u0*np.exp(-0.5*(t-a*2)*t)
#plotting analytical vs numerical solutions
ax1 = plt.subplots(1, sharex=True, figsize=(10,5))          
plt.plot(t,ua,color='black',linestyle='-',linewidth=3,label="$u_a(t)$")
plt.plot(t,u2,color='yellow',linestyle='-.',linewidth=3,label="$u_2(t)$")
plt.plot(t,u3,color='lime',linestyle='-.',linewidth=3,label = "$u_3(t)$")
plt.plot(t,u4,color='deepskyblue',linestyle='-.',linewidth=3,label = "$u_4(t)$")
plt.xlabel("t",fontsize=19) 
plt.ylabel(r' ',fontsize=19,labelpad=20).set_rotation(0)
plt.ylim([0,8])
plt.xlim([t0,tfinal]) 
plt.xticks(fontsize= 17)
plt.yticks(fontsize= 17) 
plt.legend(loc=2,fontsize=19,handlelength=3) 
plt.savefig("all.png",dpi=250)
plt.show()