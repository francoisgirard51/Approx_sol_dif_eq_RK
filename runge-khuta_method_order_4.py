# We use Runge-Khuta method of order 4: k_4 = f(t_i+dt,y_i+dt*k_3)
# to approximate the solution of the equation: dy = -t*y
# y_{i+1} approx equal y_i+(dt/6)*(k_1+2k_2+2k_3+k_4)

import numpy as np
import matplotlib.pyplot as plt

t = t_range[0]
y = y_exact[0]

y_rk4=[]
for t in t_range:
    y_rk4.append(y)
    k1 = f(t,y)
    k2 = f(t+dt/2, y+(dt/2)*k1)
    k3 = f(t+dt/2, y+(dt/2)*k2)
    k4 = f(t+dt/2, y+dt*k3)
    y = y+(dt/6)*(k1+2*k2+2*k3+k4)
    
plt.figure()
plt.plot(t_range, y_exact, label='Exact solutions of the equation y\'= -ty', c = 'red')
plt.plot(t_range, y_rk2, label='Approximation of y\'= −ty solutions by using RK2', c = 'blue')
plt.plot(t_range, y_rk4, label='Approximation of y\'= −ty solutions by using RK4', c = 'green')
plt.legend()
plt.show()
