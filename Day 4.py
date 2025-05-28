print("Welcome to Theme Park")
age = input("What is Your Age?\n")

age = int(age)
if age >= 18:
    print("You are old enough!")
    camera = input("Would you like an extra camera?y/n")
    if camera == "y":
         print("Your bill is $20")
    else:
         print("Your bill is $18")
else:
     print("You are not old enough!")

