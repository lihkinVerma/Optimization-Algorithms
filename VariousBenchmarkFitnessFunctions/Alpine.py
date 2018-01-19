import math

############################################
#    Alpine Function
############################################
D2=10
LB2=-10
UB2=10
def FitnessFunction2(x):
	sum=0
	for i in range(len(x)):
		sum=sum+abs(x[i]*(math.sin(x[i]))+(0.1*x[i]))
	return sum