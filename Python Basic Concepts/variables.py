name = "Tsunami"
print(name) #Tsunami

name = "Brook"
print(name) #Brook

#The value of a variable can be rewritten further down the code you go.

num = 4 + 2 #6

#Casting Commands!
newNum = "6"
# You cannot add newNum and num, it'll result in an error. The only way is the following:

newNum = int(newNum) #Turning newNum, which orginally holds a string, into an int.
#With that in Mind
print(newNum + num) #12

#You could turn num into a string as well:
num = str(num)

#However, adding the two would result as seen below:
print("6" + num) #66
#It dosen't add anything, merely pulls the string together... Resulting in 66

#Other functions Are:
#str(), int(), float() and bool()

#An Example from the Website

int_value = 4
print(int_value)
print(type(int_value)) #Prints the type of var a value is.

print()

float_value = float(int_value) 
print(float_value) #4.0
print(type(float_value))