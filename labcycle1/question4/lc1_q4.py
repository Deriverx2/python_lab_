#Function to check whether happy number or not
def che_hap(num):
  i=0
  while i<102:
    i+=1
    r=0
    while num>0:
      rem=num%10
      r=r+rem*rem
      num=num//10
    if r==1:
      return r
    else:
      num=r
  if r!=1:
    return r

#Function to print all happy numbers in a range
def che_ran():
  num1=int(input("\nEnter lower limit "))
  num2=int(input("Enter upper limit "))
  c=[]
  for i in range(num1,num2+1):
    if che_hap(i)==1:
      c.append(i)
  print("Happy numbers in a range:",c)


#Function to print first N happy numbers
def che_nat():
  n=int(input("\nEnter number of terms "))
  print("First %d happy numbers: " %(n),end='')
  i=1
  c=[]
  while n>0:
    if che_hap(i)==1:
      c.append(i)
      n-=1
    i+=1
  print(c,'\n')

#main part
n=int(input("\nEnter a number "))
if che_hap(n)==1:
  print(n," is a happy number")
else:
  print(n," is a sad number")
che_ran()
che_nat()