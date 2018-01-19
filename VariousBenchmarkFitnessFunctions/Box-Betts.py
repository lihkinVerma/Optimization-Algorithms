import math

############################################
#   Box-Betts Quadratic Sum Function
############################################
D8=2
LB80=0.9
UB80=1.2
LB81=9
UB81=11.2
LB82=0.9
UB82=1.2
def FitnessFunction8(x):
	f=0
	for i in range(len(x)):
		g=math.exp(-0.1*(i+1)*x[0])-math.exp(-0.1*(i+1)*x[1])-math.exp(((-0.1*(i+1))-math.exp(-i-1))*x[2])
		f=f+g
	return f