height = int(input("Enter your height: "))

if height >= 120:
    print("You can ride!")
    age = int(input("Enter your age: "))
    if age >= 18:
        photo = input("Do you want photos? y/n\n")
        if photo == "y":
            print("Your ticket price is $15")
        else:
            print("Your ticket price is $12")
    elif age < 12:
        photo = input("Do you want photos? y/n\n")
        if photo == "y":
            print("Your ticket price is $8")
        else:
            print("Your ticket price is $5")
    elif age < 18:
        photo = input("Do you want photos? y/n\n")
        if photo == "y":
            print("Your ticket price is $10")
        else:
            print("Your ticket price is $7")
else:
    print("Cannot ride")