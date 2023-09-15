limit = int(input("Limit: "))
verdict = "The consecutive sum: "
num = 1
sum = 0
while sum < limit:
    sum += num
    verdict += f"{num} + "
    num += 1
verdict += f"\b\b = {sum}"
print(verdict)