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