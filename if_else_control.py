#define a function
def flow_control(k):
	#define a stirng based on the value of k
	if(k==0):
		s = "Variable K = %d equals 0." % k
	elif(k==1):
		s = "Variable K = %d equals 1." % k
	else:
		s = "Variable k = %d does not equal 0 or 1." % k
	print(s)

def main():
	i = 0
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

if __name__ == "__main__":
	main()