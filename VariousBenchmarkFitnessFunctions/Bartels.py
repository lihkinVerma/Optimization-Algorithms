import math

############################################
#    Bartels Conn Function
############################################
D3=2
LB3=-500
UB3=500
def FitnessFunction3(x):
	return (abs(math.pow(x[0],2)+math.pow(x[1],2)+x[0]*x[1]))+abs(math.sin(x[0]))+abs(math.cos(x[1]))
