import random
def wowza():
    aiplayer = random.choice("r"+"p"+"s")
    player = str(input("Rock paper or scissor? : "))
    if aiplayer == "r":
        result =aiplayer.replace("r","rock")
    if aiplayer == "p":
        result =aiplayer.replace("p","paper")
    if aiplayer == "s":
        result =aiplayer.replace("s","scissor")
    print("AI plays", result)
    if result == player:
        print("It's a draw!")
    elif result == "scissor" and player == "rock":
        print("You won!")
    elif result == "scissor" and player == "paper":
        print("You lost!")
    elif result == "rock" and player == "scissor":
        print("You lost!")
    elif result == "rock" and player == "paper":
        print("You won!")
    elif result == "paper" and player == "rock":
        print("You lost!")
    elif result == "paper" and player == "scissor":
        print("You won!")

wowza()