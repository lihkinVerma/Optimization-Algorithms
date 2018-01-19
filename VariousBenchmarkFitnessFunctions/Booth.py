import math

############################################
#    Booth Function
############################################
D7=2
LB7=-10
UB7=10
def FitnessFunction7(x):
	return (math.pow((x[0]+2*x[1]-7),2)+math.pow((2*x[0]+x[1]-5),2))
