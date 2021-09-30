import numpy as np #import numpy library 

#integers

i = 10
print(type(i)) #print out the data type of i (integer)

a_i = np.zeros(i,dtype=np.int64) #declares an array of integers
print(type(a_i)) #returns ndarray
print(type(a_i[0])) #will return int64

#floats

x = 119.0 #floating point number
print(type(x)) #prints data type of x

y = 1.19e2 #float 119 in sci. notation
print(type(y)) #returns data type of y

z = np.zeros(1,dtype=float) #declare an array of floats
print(type(z)) #returns array
print(type(z[0])) #returns float64