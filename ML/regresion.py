import matplotlib as plt
import numpy as np

#from matplotlib import *
#from numpy import *

house_price=[245,321,279,308,199,219,405,324,319,255]
size=[1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

print(len(house_price))
print(len(size))

size2=np.array(size).reshape((-1,1))

print(size2)
regr= linear_model.LinearRegression()
regr.fit(seze2,house_price)
print('Coef: {0}'.format(regr.coef_))
print('int: {0}'.format(regr.intercept_))

def graf(form,x_range)
	x=np.array(x_range)
	y=eval(formula)
	plt.plot(x,y)
graph()
