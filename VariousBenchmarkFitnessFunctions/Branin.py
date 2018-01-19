import math

############################################
#   Branin RCOS Function
############################################
D9=3
LB90=-5
UB90=10
LB91=0
UB91=15
LB92=5
UB92=20
def FitnessFunction9(x):
	t1=x[1]
	t2=5.1*x[0]*x[0]/(4*3.14*3.14)
	t3=-6+(5*x[2]/3.14)
	t4=math.pow(t1-t2+t3,2)
	t5=10*(1-(1/(8*3.14)))*math.cos(x[0])+10
	return t4+t5
