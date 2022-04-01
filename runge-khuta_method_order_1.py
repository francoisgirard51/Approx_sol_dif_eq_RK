# We use Runge-Kutta method of order 1: k_1 = f(t_i,y_i)
# to approximate the solution of the equation: dy = -t*y

import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return -t*y

t = t_range[0]
y = y_exact[0]

y_rk1=[]
for t in t_range:
    y_rk1.append(y)
    k1 = f(t,y)
    y = y+dt*k1

plt.figure()
plt.plot(t_range, y_exact, label='Exact solutions of the equation y\'= -ty', c = 'red')
plt.plot(t_range, y_rk1, label='Approximation of y\'= −ty solutions by using RK1 method', c = 'blue')
plt.legend()
plt.show()
