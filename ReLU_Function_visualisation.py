# This program plots the value for ReLU function in the range of -20 to +20

import math

xaxis = range(-20,20)
yaxis = []

for i in xaxis:
	if i<0:
		f=0
	else:
		f=i
	yaxis.append(f)
	
import matplotlib.pyplot as plt
plt.title("Behaviour of ReLU function")
plt.scatter(xaxis,yaxis)
plt.plot(xaxis,yaxis)

plt.show()
