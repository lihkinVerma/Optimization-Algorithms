import math

############################################
#    Bird Function
############################################
D5=2
LB5=-2*3.14
UB5=2*3.14
def FitnessFunction5(x):
	sum=math.sin(x[0])*math.exp(math.pow((1-math.cos(x[1])),2))
	sum=sum+ math.cos(x[1])*math.exp(math.pow((1-math.sin(x[0])),2))
	sum=sum+ math.pow(x[0]-x[1],2)
	return sum
