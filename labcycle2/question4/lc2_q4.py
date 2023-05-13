'''Write a program to create a class Box with data members length, breadth, height, area, and volume.
Provider constructor that enables initialization with one parameter (for cube), two parameters (for square prism)
three parameters (rectangular prism). Also, provide functions to calculate area and volume.
Create a list of N boxes with random measurements and print the details of the box with maximum volume: area ratio.'''
import random

class Box:
    def __init__(self,l,b,h):
        if (b==None and h==None):
             self.length=self.breadth=self.height=l
             print("\nCube")
             print("Length:",self.length)
        elif (h==None):
            self.length=self.breadth=l
            self.height=b
            print("\nSquare Prism")
            print("Length:",self.length)
            print("Breadth:",self.breadth)
        else:
            self.length=l
            self.breadth=b
            self.height=h
            print("\nRectangle Prism")
            print("Length:",self.length)
            print("Breadth:",self.breadth)
            print("Height:",self.height)

    def Area(self):
        self.area=self.length*self.breadth
        print("Area:",self.area)

    def Volume(self):
        self.volume=self.height*self.length*self.breadth
        print("Volume:",self.volume)
    
    def details(self):
        self.Area()
        self.Volume()
      
    def ratio(self):
        ratio=self.volume/self.area
        return ratio
    

c=[]
r=[]
s=[]
cube_ratio=[]
sqr_ratio=[]
rect_ratio=[]
n= int(input("\nEnter range : "))
for i in range(n):
  #cube
  c.append("")
  c[i]=(Box(random.randint(1,100),None,None))
  c[i].details()
  cube_ratio.append(c[i].ratio())

  #sqr
  s.append("")
  s[i]=Box(random.randrange(1,100),random.randint(1,100),None)
  s[i].details()
  sqr_ratio.append(s[i].ratio())

  #rect
  r.append("")
  r[i]=Box(random.randint(1,100),random.randint(1,100),random.randint(1,100))
  r[i].details()
  rect_ratio.append(r[i].ratio()) 
  rect_ratio.append(r[i].ratio()) 

full_ratio=[max(cube_ratio),max(sqr_ratio),max(rect_ratio)] #getting the highest ratio from each shape
ind=full_ratio.index(max(full_ratio))
print()
if ind==0:                                                  #printing the shape details ofthe highest ratio shape
  pos=int(cube_ratio.index(max(cube_ratio)))
  print("Max cube",max(cube_ratio))
  print("Most area to volume ratio is for Cube ")
  c[pos].details()
  print(" The ratio is: ",c[pos].ratio())
elif ind==1:
  pos=sqr_ratio.index(max(sqr_ratio))
  print("Most area to volume ratio is for Square Prism")
  s[pos].details()
  print("The ratio is: ",s[pos].ratio())
elif ind==2:
  pos=rect_ratio.index(max(rect_ratio))
  print("Most area to volume ratio is for Rectangle Prism")
  r[pos].details()
  print("The ratio is: ",r[pos].ratio())