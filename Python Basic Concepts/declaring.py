def main(): #Defines the Start of a Python Code
    print("Testing Things Out.")
    secondaryFunction()

def secondaryFunction():
    print("Trying to figure out if this works at all.")

if __name__ == '__main__':
    main()

name = "Rose" #This is an inline comment.
#This is a block comment.

def caculateMinutes(sec):
    #This caculates the ammount of minutes from a given ammount of seconds.
    minutes = sec / 60
    return minutes #Returns the result of seconds divided by 60.


def square(num):
    numSqu = num ** 2
    return numSqu

print(square(5)) #returns 25