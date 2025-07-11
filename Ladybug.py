t = int(input())
def number_check():
    n = int(input())
    a = input()
    b = input()
    list_a = list(a)
    list_b = list(b)
    new_lista = []
    new_listb =[]
    i = 0
    p = 0
    r = 0
    zero_a = 0
    zero_b = 0

    for i in range(n):
        if i % 2==0:
            new_lista.append(list_a[i])
            new_listb.append(list_b[i])

        else:
            new_listb.append(list_a[i])
            new_lista.append(list_b[i])


    for p in range(n):
        if new_lista[p] == "0":
            zero_a += 1

        if new_listb[p] == "0":
            zero_b += 1

    if zero_a >= n/2 and zero_b >= n/2:
        print("YES")
    else :
        print("NO")

for i in range(t):
    number_check()
