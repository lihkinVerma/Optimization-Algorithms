import math

############################################
#    Beale Function
############################################
D4=2
LB4=-4.5
UB4=4.5
def FitnessFunction4(x):
	sum=math.pow((1.5-x[0]+x[0]*x[1]),2)
	sum=sum+math.pow((2.25-x[0]+x[0]*x[1]*x[1]),2)
	sum=sum+math.pow((2.625-x[0]+x[0]*x[1]*x[1]*x[1]),2)
	return sum
