t = int(input())
for t in range(t):
    n = int(input())
    cakes = list(map(int, input().split()))
    diff = []
    SP = []
    CP = []
    value = 0
    for each_number in cakes:
        for t in range(len(cakes)):
            if cakes[t] > each_number:
                value += each_number*50
            elif cakes[t] < each_number:
                value += cakes[t]*50
            elif cakes[t] == each_number:
                value += each_number*50
        SP.append(value)
        value = 0
        value_cp = each_number*30*len(cakes)
        CP.append(value_cp)
        value_cp = 0
    for t in range(len(SP)):
        diff.append(SP[t] - CP[t])
    print(max(diff))