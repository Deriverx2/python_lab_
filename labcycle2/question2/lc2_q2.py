#Rotate elements by k to right
def rotate(l1):
  k=int(input("\nEnter position "))
  l2=[i for i in l1[-k:]]
  for i in l1[:-k]:
    l2.append(i)
  print(l2)

#list to tuple using list comprehension
def tupleConversion(l1):
  print("\nTuple Conversion")
  tup=tuple(i for i in l1)
  return(tup)

#Remove duplicates from tuple and covert to list
def removeDuplicates(t1):
  print("\nRemove Duplicates from Tuple")
  res = tuple(set(t1))
  print("The tuple after removing duplicates : " + str(res))
  l1=list(res)
  print("The tuple converted to list : " + str(l1))
  return l1

#create list of function x^2-x
def FunctionList(l1):
  l2=[i*i-i for i in l1]
  print("\nFunction List : "+str(l2))
  return l2

#Sort and merge two lists
def SortMerge(l1,l2):
  l3=sorted(l1+l2)
  print("\nSorted And Merged List : "+str(l3))
  return(l3)

def main():
  strin=str(input("\nEnter numbers with space separated\n"))
  l1=strin.split()
  l1=[int(i) for i in l1]
  print(l1)
  rotate(l1)
  t1=tupleConversion(l1)
  print(t1)
  l2=removeDuplicates(t1)
  l3=FunctionList(l2)
  l4=SortMerge(l2,l3)

main()