#Write a program to print the factors of a number 
x=int(input("Enter a number: "))
for i in range(1,(x//2)+1):
    if x%i==0:
        print(i,end=' ')