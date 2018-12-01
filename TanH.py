# Author: Suri Bhasker Sri Harsha
#       : MS- Research Scholar
#       : Computer Science Department
#  	 : IIT Tirupati

# This function plots the values for sigmoid function in the range of -20 to +20

import math

xaxis = range(-20,20)
yaxis = []

for i in xaxis:
	f = (2/(1+math.exp(-2*i)))-1
	yaxis.append(f)
	
import matplotlib.pyplot as plt
plt.title("Behaviour of sigmoid function")
plt.scatter(xaxis,yaxis)
plt.plot(xaxis,yaxis)
plt.grid()
plt.show()
