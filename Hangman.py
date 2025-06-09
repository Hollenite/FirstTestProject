stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = ["ardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
#Test code
print(chosen_word)
length_of_chosen_word = len(chosen_word)
display = ""
for n in range(length_of_chosen_word):
    display += "_"
list_of_letters = list(display)
new_display = ""
# print(list_of_letters)
# while new_display != chosen_word:
while not lives < 0 and new_display != chosen_word:
    old_display = "".join(list_of_letters)
    guess = input("Guess a letter: ").lower()
    for n in range(length_of_chosen_word):
        if chosen_word[n] == guess:
            list_of_letters[n] = chosen_word[n]
    # print(list_of_letters)
    new_display = "".join(list_of_letters)
    # if lives < 1:
    #     print("You lost")
    if new_display == old_display:
        print(stages[lives])
        lives -= 1
        # print("wrong word")
    print(new_display)
if lives < 1:
    print("You lost")
if new_display == chosen_word:
    print("You won!")

# guess2 = input("Guess a letter: ").lower()
# for n in range(length_of_chosen_word):
#     if chosen_word[n] == guess2:
#         list_of_letters[n] = chosen_word[n]
# new_display2 = "".join(list_of_letters)
# print(new_display2)

# if guess in chosen_word:
#     print("You guessed the word!")
# else:
#     print("Sorry, you guessed wrong.")



