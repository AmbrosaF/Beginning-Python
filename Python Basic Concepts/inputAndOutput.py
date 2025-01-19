name = input("What's your name?") #Asks for User's Name
print("Hello, nice to meet you {}!" .format(name)) #Another way to format such is the following:
# print("Hello, nice to meet you" + name + "!")

myName = "Rose"
age = "22" #Bare in mind, this produces a string, thus holds no numerical value.
ageNum = 22 #This would be able to be used within equestions, but not within strings without being transfered.

print("Very nice to meet you {}! My name is {}, and I am {} years old!" .format(name,myName,age)) #They're shown in order of typed within the format command.
# Very nice to meet you {yourName}! My name is Rose, and I am 22 years old!

print(age == ageNum) #False
