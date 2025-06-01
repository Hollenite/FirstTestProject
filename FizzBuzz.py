# total_sum = 0
# for number in range(1, 101):
#     total_sum += number
# print(total_sum)
# # print(101 * 50)
#
# target = int(input("number\n"))
#
# total = 0
# for number in range(2 , target+1, 2):
#     total += number
#
# print
target = int(input())
for number in range(1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

























