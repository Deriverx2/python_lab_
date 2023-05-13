from prettytable import PrettyTable
myTable = PrettyTable(["Month", "Rabbit Pair Count"])
Apair=1
n=int(input("\nEnter number of months :"))
month=1
myTable.add_row([month, Apair])
month+=1
Bpair=Apair
myTable.add_row([month, Bpair])
while month<n:
  month+=1
  pair=Apair+Bpair
  Apair=Bpair
  Bpair=pair
  myTable.add_row([month, pair])
print(myTable,'\n')