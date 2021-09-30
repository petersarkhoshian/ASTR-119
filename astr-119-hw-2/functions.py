import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x) #return the numpy function e^x

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #calls the function expo


#define a main function
def main():
	n = 10 #provide a flat value for n

	if(len(sys.argv)>1): #check if there is a command line argument provided
		n = int(sys.argv[1]) # if argument was provided, use it for n

	show_expo(n) #calls the subroutine above

#run the main function
if __name__ == "__main__":
	main()