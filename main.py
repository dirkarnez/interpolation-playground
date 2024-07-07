

import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import CubicSpline

a_x=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.7,5, 5.5]
a_y=[1610, 1625, 1623, 1605, 1557, 1480, 1385, 1230, 1150, 1000, 500]

b_x=[4, 4.5, 4.7, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
b_y=[1410, 1380, 1355, 1310, 1240, 1160, 1060, 950, 840, 720, 580, 430, 245]

c_x=[2.5, 3, 3.5, 4, 4.5, 4.7, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
c_y=[1635, 1630, 1625, 1620, 1600, 1588, 1570, 1530, 1480, 1430, 1370, 1300, 1230, 1140, 1060, 970, 870, 760, 630, 480, 355]

d_x=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.7, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]
d_y=[2080, 2075, 2070, 2065, 2060, 2050, 2040, 2035, 2033, 2030, 2010, 1970, 1930, 1880, 1820, 1760, 1690, 1610, 1530, 1440, 1350, 1260, 1150, 1040, 900, 680, 200]

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



# def f(o):
#   sum = 0
#   for i in range(n+1):
#     prod = y[i]
#     for j in range(n+1):
#       if i!= j:
#         prod=prod*(o-x[j])/(x[i]-x[j])
#     sum = sum + prod
#   return sum

def my_plot(x, y):
  range = np.linspace(min(x),max(x),500)
  plot.plot(x, y,marker='o', ls='', markersize=10)
  plot.plot(range, CubicSpline(x, y)(range))


my_plot(a_x, a_y)
my_plot(b_x, b_y)
my_plot(c_x, c_y)
my_plot(d_x, d_y)

plot.plot(np.random.uniform(0, 10, 10), np.random.uniform(0, 10, 10), color='red', marker='x', ls='', markersize=10)



plot.show()

