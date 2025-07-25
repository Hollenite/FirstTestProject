t = int(input())
n = int(input())
cakes = (input()).split()
print(cakes)
value = -1
number = []
value_corresponding_toNumber = []

for each_number in cakes:
    for t in range(len(cakes)):
        if each_number <= cakes[t]:
            value += 1
    value_corresponding_toNumber.append(value)
    number.append(each_number)
    value = -1

print(number)
print(value_corresponding_toNumber)
x_value = max(value_corresponding_toNumber)
print(x_value)

