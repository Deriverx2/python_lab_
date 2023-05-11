import math

#function to read three sides of triangle
def read_sides():
  a1=float(input("\nEnter first side of a triangle: "))
  a2=float(input("Enter second side of a triangle: "))
  a3=float(input("Enter third side of a triangle: "))
  return a1,a2,a3

#function to check triangle
def check(tri):
  if tri[0]+tri[1]>tri[2] and tri[1]+tri[2]>tri[0] and tri[2]+tri[0]>tri[1]:
    return True
  else:
    return False


#function for area of triangle
def get_area(a1,a2,a3):
  s=(a1+a2+a3)/2
  area=math.sqrt(s*(s-a1)*(s-a2)*(s-a3))
  return area

#Area contribution
def get_per(total,a):
  per=(a/total)*100
  return per

#main part
t1=read_sides()
while(check(t1)==False):
  print("The given triangle does not satisfy inequality theorem!")
  print("Try again!")
  t1=read_sides()
area_t1=get_area(t1[0],t1[1],t1[2])
print("\nArea of first triangle=",area_t1)

t2=read_sides()
while(check(t2)==False):
  print("The given triangle does not satisfy inequality theorem!")
  print("Try again!")
  t2=read_sides()
area_t2=get_area(t2[0],t2[1],t2[2])
print("\nArea of second triangle=",area_t2)

sum=area_t1+area_t2
print("\nTotal area of traingles=",sum)
print("\nFirst triangle contributes ",get_per(sum,area_t1),"%")
print("\nSecond triangle contributes ",get_per(sum,area_t2),"%\n")