from itertools import combinations

t = int(input())
for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    remainders = []
    max_remainders =[]
    # print(numbers)
    # if only one x , ignore all tuples with x, if more than one it does not affect
    for each_number in numbers:
        index_value = numbers.index(each_number)
        numbers.remove(each_number)
        pairs = list(combinations(numbers, 2))
        # print(pairs)
        for each_tuple in pairs:
            if each_tuple[0] == each_tuple[1]:
                pairs.remove(each_tuple)
                pairs.append((each_number , 0))
        numbers.insert(index_value, each_number)
        # print(pairs)
        sum_pair = list(map(sum, pairs))
        # print(sum_pair)
        for l in range(len(sum_pair)):
            remainders.append(each_number % sum_pair[l])
        max_remainders.append(max(remainders))
        # print(max_remainders)
        remainders.clear()
        pairs.clear()
        sum_pair.clear()
    print(max(max_remainders))
    max_remainders.clear()


    # for i in range(n):
    #     if i == 0:
    #         remainders.append(numbers[i] % (numbers[i + 1] + numbers[i+2]))
    #     elif i == 1:
    #         remainders.append(numbers[i] % (numbers[i - 1] + numbers[i + 1]))
    #     elif i == 2:
    #         remainders.append(numbers[i] % (numbers[i - 1] + numbers[i - 2]))
    #     else:
    #         print("Error") // ONLY WORKS FOR 3 NUMBERS

