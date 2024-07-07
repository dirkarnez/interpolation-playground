

import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import CubicSpline

x=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.7,5, 5.5]
y=[1610, 1625, 1623, 1605, 1557, 1480, 1385, 1230, 1150, 1000, 500]

n=len(x)-1
prange = np.linspace(min(x),max(x),500)

cs = CubicSpline(x, y)

plot.plot(x,y,marker='o', color='r', ls='', markersize=10)

# def f(o):
#   sum = 0
#   for i in range(n+1):
#     prod = y[i]
#     for j in range(n+1):
#       if i!= j:
#         prod=prod*(o-x[j])/(x[i]-x[j])
#     sum = sum + prod
#   return sum

# plot.plot(prange, f(prange))

plot.plot(prange, cs(prange))
plot.show()


