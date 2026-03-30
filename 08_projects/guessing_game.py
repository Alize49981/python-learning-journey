import random

number = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct! 🎉")
            break
        elif guess < number:
            print("Too low 📉")
        else:
            print("Too high 📈")

    except ValueError:
        print("Please enter a valid number!")