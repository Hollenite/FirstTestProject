
t = int(input())
n = int(input())
S = input()
list_S = list(S)
new_list = []
litUp = False

if n % 2 == 0:
    count = 0
    while count < n:
        combined = list_S[count] + list_S[count + 1]
        new_list.append(combined)
        # new_list.append(list_S[count])
        # new_list.append(list_S[count+1])
        count += 2
        # print(new_list)
        combined = ""
else:
    count = 0
    while count < n:
        if count == n-1:
            new_list.append(list_S[count])
            count += 2
            # print(new_list)
        else:
            combined = list_S[count] + list_S[count + 1]
            new_list.append(combined)
            combined = ""
            # new_list.append(list_S[count])
            # new_list.append(list_S[count+1])
            count += 2
            # print(new_list)
print(new_list)
# new_count = 0
# while new_count < n:
#     print(new_count)
length = len(new_list)
# print(length)
for i in range(length):
    if new_list[length-1] in [0b01 or 10 or 11 or 1]:
        print(new_list[length - 1])
        litUp = True
        print(litUp)
        # new_count += 2
    else:
        litUp = False
        break
    # if new_list[length-1] == 00 or 0:
    #     print(new_list[length-1])
    #     litUp = False
    #     print(litUp)
    #     break
        # new_count += 2

if litUp:
    print("YES")
else:
    print("NO")

# word = "Hello"
# list1 = ["Hello"]
# if list1[0] == word:
#     print("YES")
# else:
#     print("NO")


# for i in range(n):
    # if list_S[i] == "0":
    #     isWorking = False
    # if not isWorking:
    #     litUp = False
    #     continue
    # if isWorking:
    #     if list_S[i+1] == "0":
    #         # isWorking = True
    #         litUp = True
    #         continue

    # if list_S[i] == "1":
    #     if list_S[i+1] == "0":
    #     lipUp_list.append(