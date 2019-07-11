import matplotlib.pyplot as plt
from matplotlib import *

x=[1,2,3,4,5]

plt.plot(x,x, 'bo',label='lineal')
plt.plot(x,x**x,'r', label='c')
plt.legend()
plt.xlabel('x')
plt.show()
