#hollow sqaure
x=int(input("Enter:"))
#end='' function prints hing inside '' instead of going to /n
for i in range(x):
    print('*',end='')
print('')
for i in range(x-2):
    print('*',end='')
    for j in range(x-2):
        print(' ',end='')
    print('*')
for i in range(x):
    print('*',end='')