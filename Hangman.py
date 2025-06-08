word_list = ["ardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
#Test code
print(chosen_word)
guess = input("Guess a letter: ").lower()
length_of_chosen_word = len(chosen_word)
display = ""
for n in range(length_of_chosen_word):
    display += "_"
print(display)
for n in range(length_of_chosen_word):
    if guess == chosen_word[n]:
        print("right")
    else:
        print("wrong")
# if guess in chosen_word:
#     print("You guessed the word!")
# else:
#     print("Sorry, you guessed wrong.")



