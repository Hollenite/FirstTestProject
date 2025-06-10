def prime_checker(number):
    x = 0
    for each_number in range(2, number):
        if number % each_number == 0:
            x += 1
    if x > 0:
        print(f"{number} is not prime")
    else:
        print(f"{number} is prime")


n = int(input())
prime_checker(number=n)