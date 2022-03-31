# Initial function 'y_exact' with defined ranged values

import numpy as np
import matplotlib.pyplot as plt

dt=0.1
t_range = np.arange(-3,3+dt,dt)
y_exact = np.exp(-t_range**2/2)

plt.figure()
plt.plot(t_range, y_exact, label='function y_exact')
plt.legend()
plt.show()
