print("************************")
print("Welcome to guessing game")
print("************************")

secret_number = 12

number = int(input("Input your number: "))
print("Your number is", number)

if number == secret_number:
    print("Congrats you are right")
elif number > secret_number:
    print("The secret number is biggest")
else:
    print("The secret number is smallest")
