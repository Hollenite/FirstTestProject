import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F"]
numbers = ["0", "1", "2","3", "4", "5" "6", "7", "8", "9", "10"]
symbols = ["!", "#" , "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to Password Generator")

nr_letters = int(input("How many letters would you like to generate?\n"))
nr_symbols = int(input("How many symbols would you like to generate?\n"))
nr_numbers = int(input("How many numbers would you like to generate?\n"))

random_letters = random.sample(letters, nr_letters)
random_symbols = random.sample(symbols, nr_symbols)
random_numbers = random.sample(numbers, nr_numbers)

list1 = random_letters + random_symbols + random_numbers
password_list = random.sample(list1, int(nr_letters) + int(nr_symbols) + int(nr_numbers))
# print(list1)
# print(password)
password = ""
# password = "".join(password_list)
# print(password)
for each_letter in password_list:
    password += each_letter

print(f"Your password is {password}")