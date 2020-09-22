print("************************")
print("Welcome to guessing game")
print("************************")

secret_number = 12

level = int(input("Choose easy level (1, 2, 3): "))
attempts = level * 3

while attempts >= 1:
    number = int(input("Input your number: "))
    print("Your number is  {}".format(number))

    if number == secret_number:
        print("Congrats you are right")
        break
    elif number > secret_number:
        print("The secret number is biggest")
    else:
        print("The secret number is smallest")

    attempts -= 1

