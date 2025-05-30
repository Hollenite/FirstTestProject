rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list1 = [rock, paper, scissor]
list2 = ["rock", "paper", "scissor"]

print("Press 0 for rock, 1 for paper, 2 for scissor")
user_input = input()
if user_input != "0" and user_input != "1" and user_input != "2":
    print("PLEASE CHOOSE A CORECT NUMBER!!!")


import random
random_number = random.randint(0, 2)
#
# if user_input == "0":
#     print("You chose rock!")
#     print(rock)
# elif user_input == "1":
#     print("You chose paper!")
#     print(paper)
# else:
#     print("You chose scissor!")
#     print(scissor)
#
# if random_number == 0:
#     print("I chose rock!")
#     print(rock)
# elif random_number == 1:
#     print("I chose paper!")
#     print(paper)
# else:
#     print("I chose scissor!")
#     print(scissor)

user_input2 = list2[int(user_input)]
user_input3 = list1[int(user_input)]
print(f'You chose {user_input2}')
print(user_input3)

random_number2 = list2[random_number]
random_number = list1[int(random_number)]
print(f'I choose {random_number2}')
print(random_number)

if user_input3 == rock:
        if random_number == paper:
            print("You lose")
        elif random_number == scissor:
            print("You win")
        elif random_number == rock:
            print("Its a Draw")
if user_input3 == paper:
        if random_number == rock:
            print("You win")
        elif random_number == scissor:
            print("You lose")
        elif random_number == paper:
            print("its a Draw")
if user_input3 == scissor:
        if random_number == rock:
            print("You lose")
        elif random_number == paper:
            print("You win")
        elif random_number == scissor:
            print("Its a Draw")




