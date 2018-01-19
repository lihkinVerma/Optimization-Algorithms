import math

############################################
#    Acley's function
############################################
D1=10
LB1=-35
UB1=35
def FitnessFunction1(x):
	t1=0
	t2=0
	for i range(len(x)):
		t1=t1+x[i]*x[i]
		t2=t2+math.cos(2*3.14*x[i])
	t3=math.sqrt(t1/len(x))
	t4=t2/len(x)
	t5=-20*math.exp(-0.02*t3)-math.exp(t4)+20+math.exp(1)
	return t5