#String are sequence of characters
s1="hello"
s2="world"
print(s1,type(s1))
print(s2,type(s2))

#conversion of int to sting
a=123
print(a,type(a))
a=str(a)
print(a,type(a))

#string concatenation
s3=s1+' '+s2
print(s3)

#the %symbol can be used as a format specifier that allows to concatenate in a given format
s4='%s_%s'%(s1,s2)
print(s4)

#length of a string can be obtained by len function
s='Hi, How are you?'
print(s)
print("length=",len(s))

#coneverts a string to uppercsase
print(s.upper())

#coneverts a string to lowercase
print(s.lower())

#capitalizes the first letter of a string
print(s.capitalize())

#split function splits between spaces into a list
print(s.split())

#join function joints together strings in a list
ss=s.split(' ')
print(ss)
print(' '.join(ss))

#find function finds the first position of element(returns -1 if element not found )
print(s.find("H"))
print(s.find('q'))