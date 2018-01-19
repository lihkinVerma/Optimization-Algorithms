import math

############################################
#    Bohachevsky Function
############################################
D6=2
LB6=-100
UB6=100
def FitnessFunction6(x):
	sum=x[0]*x[0] + 2*x[1]*x[1]
	sum=sum- 0.3*math.cos(3*3.14*x[0])+0.7
	sum=sum- 0.4*math.cos(0.4*3.14*x[1])
	return sum
