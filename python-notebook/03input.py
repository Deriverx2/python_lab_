#input function can be used to get input
s=input()
print(s)

#input function can have print string input
name=input("Enter your name: ")
print("Your name is ",name)

#normally input function takes input as string
print(type(s))
print(type(name))

age=int(input("Enter your age: "))
#age=int(age) changes string input to integer
print("Your age is ",age)
print(type(age))

weight=float(input("Enter your weight: "))
print("Your weight is ",weight)
print(type(weight))