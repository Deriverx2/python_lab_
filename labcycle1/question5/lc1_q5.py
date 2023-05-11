#Function to print substrings
def substrings(a):
  print("ALL POSSIBLE SUBSTRINGS:")
  b=[]
  for i in range(len(a)):
    for j in range(i+1,len(a)+1):
      if a[i:j] not in b:
        b.append(a[i:j])
  print(b)

#function to print substrings of length K
def sub_klen(a):
  k=int(input("\nEnter length required for substrings "))
  print("SUBSTRINGS OF LENGTH ",k)
  b=[]
  for i in range(len(a)-k+1):
    b.append(a[i:i+k])
  print(b)

#function to print all substrings of length K with N distinct characters.
def distinctSub(a):
  k=int(input("\nEnter length required for substrings "))
  n=int(input("Enter number of required distinct characters "))
  c=[]
  print("SUBSTRINGS OF LENGTH %d WITH %d DISTINCT CHARACTERS"%(k,n))
  for i in range(len(a)-k+1):
    b=(a[i:i+k])
    if len(set(b))==n:
      c.append(b)
  print(c)

#function to print substring of maximum length with N distinct characters.
def maxDistinct(a):
  n=int(input("\nEnter number of required distinct characters "))
  k=len(set(a))
  print("\nSubstring of maximum length with ",n," distinct characters")
  c=[]
  for i in range(len(a)-k+1):
    b=(a[i:i+k])
    if len(set(b))==n:
      c.append(b)
  print(c)

#function to print all palindrome substrings
def palindrome_substring(a):
  print("\nPalindrome substrings are:")
  c=[]
  for i in range(len(a)):
    for j in range(i+1,len(a)+1):
      b=a[i:j]
      if b==b[::-1]:
        c.append(b)
  print(c,'\n')

#main part
a=str(input("\nEnter a string value "))
substrings(a)
sub_klen(a)
distinctSub(a)
maxDistinct(a)
palindrome_substring(a)