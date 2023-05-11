#functin for getting a 4 digit number
def get():
  p=int(input("Enter a four digit number: "))
  return p
  
#function to check whether 4 digit number
def check(n):
  p=n
  count=0
  while p>0:
    p=p//10
    count=count+1
  return count

#function for sum of digits
def digit_sum(n):
  p=n
  s=0
  while p>0:
    s=s+p%10
    p=p//10
  return s

#function for reversing
def digit_reverse(n):
  p=n
  s=0
  while p>0:
    s=s*10+p%10
    p=p//10
  return s

#function for difference between the product of digits at the odd position
#and the product of digits at the even position.
def digit_difference(n):
  p=n
  op=1
  ep=1
  d=1
  while p>0:
    i=p%10
    p=p//10
    if d%2==0:
      ep=ep*i
    else:
      op=op*i
    d=d+1
  s=ep-op
  return s

#main part
num=get()
while(check(num)!=4):
  print("Error: Invalid entry")
  num=get()
sum=digit_sum(num)
reverse=digit_reverse(num)
difference=digit_difference(num)
print("sum of digits=",sum)
print("reverse=",reverse)
print("difference=",difference)