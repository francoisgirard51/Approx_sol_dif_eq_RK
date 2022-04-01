# We use Runge-Kutta method of order 2: k_2 = f((t_i+dt/2),(y_i+dt/2)*k_1) 
# to approximate the solution of the equation: dy = -t*y

import numpy as np
import matplotlib.pyplot as plt

t = t_range[0]
y = y_exact[0]

y_rk2=[]
for t in t_range:
    y_rk2.append(y)
    k1 = f(t,y)
    k2 = f(t+dt/2, y+(dt/2)*k1)
    y = y+dt*k2
    
plt.figure()
plt.plot(t_range, y_exact, label='Exact solutions of the equation y\'= -ty', c = 'red')
plt.plot(t_range, y_rk2, label='Approximation of y\'= −ty solutions by using RK2', c = 'lightgreen')
plt.legend()
plt.show()
