# states = ["State1", "State2", "State3", "State4"]
#
# states.append("State5")
# states.extend(["State9", "State6", "State7", "State8"])
#
# print(states[-1])

name = ["a", "b", "c", "d", "e", "f"]
import random
number_of_people = int(len(name))
random_number = random.randint(0, number_of_people - 1)

person = name[random_number]
print("The person who will pay is " + person)

# number = random.randint(0 , 5)
#
# if number == 0:
#     print("a")
# elif number == 1:
#     print("b")
# elif number == 2:
#     print("c")
# elif number == 3:
#     print("d")
# elif number == 4:
#     print("e")
# else:
#     print("f")