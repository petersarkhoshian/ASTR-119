#string

s = "I am a string."
print(type(s)) #returns str

#boolean

yes = True #boolean true
print(type(yes)) 

no = False #boolean false
print(type(no))

#List -- orders and changeable, represented in brackets

alpha_list = ["a", "b", "c"] #list initialization 
print(type(alpha_list)) #returns tuple
print(type(alpha_list[0])) #returns string
alpha_list.append("d") #adds "d" to the end of the list
print(alpha_list) #prints list

#Tuple -- ordered and unchangeable, represented in parenthesis

alpha_tuple = ("a", "b", "c") #tuple initialization
print(type(alpha_tuple)) #returns tuple

try: #attempts the following line
	alpha_tuple[2] = "d" #will fail and raise TypeError
except TypeError: #when TypeError occurs, run the following line
	print("We can't add elements to tuples!") #prints message in ""
print(alpha_tuple) #prints tuple