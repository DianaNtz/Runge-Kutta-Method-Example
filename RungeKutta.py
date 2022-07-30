"""
@author: Diana Nitzschke
"""
import numpy as np
import matplotlib.pyplot as plt
t0=0
tfinal=10
dt=0.12
steps=int((tfinal-t0)/dt)
u0=0.0000001
a=6
def f(t,u):
    return -(t-a)*u
t=np.empty(steps+1, dtype='double')
tn=t0
u2=np.empty(steps+1, dtype='double')
un2=u0
for i in range(0,steps+1):    
    t[i]=tn
    #Runge Kutta second
    u2[i]=un2
    k1=dt*f(tn,un2)
    k2=dt*f(tn+0.5*dt,un2+0.5*k1)
    un2=un2+k2
    tn=tn+dt
ua=u0*np.exp(-0.5*(t-a*2)*t)
ax1 = plt.subplots(1, sharex=True, figsize=(10,5))          
plt.plot(t,ua,color='black',linestyle='-',linewidth=3,label="$u_a(t)$")
plt.plot(t,u2,color='yellow',linestyle='-.',linewidth=3,label="$u_2(t)$")
plt.xlabel("t",fontsize=19) 
plt.ylabel(r' ',fontsize=19,labelpad=20).set_rotation(0)
plt.ylim([0,8])
plt.xlim([t0,tfinal]) 
plt.xticks(fontsize= 17)
plt.yticks(fontsize= 17) 
plt.legend(loc=2,fontsize=19,handlelength=3) 
plt.show()