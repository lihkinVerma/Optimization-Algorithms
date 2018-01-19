import math

############################################
#   Brent Function
############################################
D10=2
LB10=-10
UB10=10
def FitnessFunction10(x):
	t1=math.pow(x[0]+10,2)
	t2=math.pow(x[1]+10,2)
	t3=-(x[0]*x[0])-(x[1]*x[1])
	t4=math.exp(t3)
	return t1+t2+t4

