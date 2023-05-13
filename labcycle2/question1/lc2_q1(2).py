def rabbit(num):
   Apair=1
   month=1
   print("-"*50)
   print("\tMonth\t|\tRabbit Pair Count")
   print("-"*50)
   print("\t",month,'\t|\t', Apair)
   print("-"*50)
   month+=1
   Bpair=Apair
   print("\t",month,'\t|\t', Bpair)
   print("-"*50)
   while month<n:
     month+=1
     pair=Apair+Bpair
     Apair=Bpair
     Bpair=pair
     print("\t",month,'\t|\t', pair)
     print("-"*50)

n=int(input("\nEnter number of months :"))
rabbit(n)