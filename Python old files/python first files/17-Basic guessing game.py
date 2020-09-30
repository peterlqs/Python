secretword= "dolphin"
guess = ""
guesscount= 0
guesslimit= 3
outofguesses = False

while guess != secretword and not outofguesses : #!= means not equal
    if guesscount < guesslimit :
       guess = input("Enter guess: ")
       guesscount += 1
    else:
       outofguesses = True
if outofguesses:
    print("Game over")
else:
    print("You win!")
