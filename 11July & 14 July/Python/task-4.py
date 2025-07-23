import random

user = int(input("Enter a number: "))
num = random.randint(1, 50)
attempts = 1
while user != num:
    attempts += 1
    if user > num:
        print("Too high")
    elif user < num:
        print("Too low")
    user = int(input("Enter a number again: "))

print("You guessed correctly in", attempts, "attempts")