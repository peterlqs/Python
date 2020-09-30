import random
value = random.randint(1,20)
guess = int(input("Type in a number: "))
while guess!= value:
    if guess < value:
        print("Your guess is too low")
        guess = int(input("Guess again: "))
    if guess > value:
        print("Your guess is too high")
        guess = int(input("Guess again: "))


print("You're right!")


