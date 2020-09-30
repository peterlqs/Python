import random
value = random.randint(1,20)
def idk():
    guess = int(input("Type your guess: "))
    if guess > value:
        print("Guess again, ur guess is too high")
        idk()
    elif guess < value:
        print("Guess again, ur guess is too low")
        idk()
    else:
        print("You're right!")
idk()