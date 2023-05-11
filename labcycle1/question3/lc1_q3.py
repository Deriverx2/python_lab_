#Details of employee
def get_data():
  name=str(input("\nEnter name:"))
  code=str(input("Enter employee code:"))
  basic_pay=int(input("Enter basic pay in rupees:"))
  return name,code,basic_pay

#Area contribution
def get_per(a,b):
  per=(a*b)/100
  return per
  
#Gross salary calculation
def calc_salary(bp):
  if bp<10000:
    gs=bp+get_per(bp,5)+get_per(bp,2.5)+500
  elif bp<30000:
    gs=bp+get_per(bp,7.5)+get_per(bp,5)+2500
  elif bp<50000:
    gs=bp+get_per(bp,11)+get_per(bp,7.5)+5000
  else:
    gs=bp+get_per(bp,25)+get_per(bp,11)+7000
  return gs

#Deduction calculation
def calc_deduction(bp):
  if bp<10000:
    d=20+get_per(bp,8)
  elif bp<30000:
    d=60+get_per(bp,8)
  elif bp<50000:
    d=60+get_per(bp,11),get_per(bp,11)
  else:
    d=80+get_per(bp,12)+get_per(bp,20)
  return d

nam,cod,bp=get_data()
net=calc_salary(bp)-calc_deduction(bp)
print("\n\n\n\t\t\tPAY SLIP")
print("\n\t\tEmployee name:",nam.capitalize())
print("\n\t\tEmployee code:",cod)
print("\n\t\tBasic salary: ₹",bp)
print("\n\t\t----------------------------")
print("\n\t\tGross salary: ₹",calc_salary(bp))
print("\n\t\tDeduction: ₹",calc_deduction(bp))
print("\n\t\tNet salary: ₹",net,"\n")