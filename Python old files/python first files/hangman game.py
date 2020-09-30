import random
from words import listofwords
def get_word():
    secret = random.choice(listofwords)
    return secret.upper()

def play(secret):
    wordlength = "_" * len(secret)
    wordguessed = []
    letterguessed = []
    guessed= False
    tries = 6
    print("Let's play Hangman!")
    while not guessed and tries > 0:
        guess = input("Type a letter or word: ").upper()
        if len(guess) ==1:
            if guess in letterguessed:
                print("You already guessed the letter.")
            elif guess not in secret:
                print(guess," is not in the word.")
                tries -= 1
                letterguessed.append(guess)
                print("Letter guessed:","".join(letterguessed))
            else:
                print("Good job", guess, "is in the word.")
                letterguessed.append(guess)
                print("Letter guessed:","".join(letterguessed))
                secretlist = list(wordlength)
                appear = [i for i, letter in enumerate(secret) if letter==guess]
                for index in appear:
                    secretlist[index] = guess
                wordlength = "".join(secretlist)
                if "_" not in wordlength:
                    guessed= True

        elif len(guess) == len(secret):
            if guess in wordguessed:
                print("You already guessed the word", guess, "!")
            elif guess != secret:
                print(guess, "is not the word.")
                wordguessed.append(guess)
                tries -=1
            else:
                guessed = True
                wordlength = secret
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(wordlength)
    if guessed:
        print("Congrats you guessed the word!")
    else:
        print("You lost!, The word was ", secret,"!")

def display_hangman(tries):
    stages = ["""
              _____________
              |           |
              |   R.I.P   |
              |           |
              |           |
            __|___________|__
            """,
              """
                -------------
                |           |
                |         __|__
                |         |___|   
                |          /|\\
                |           |
                |          / \\
                |
            ----------
              """,
              """
                -------------
                |           |
                |         __|__
                |         |___|   
                |           |\\
                |           |
                |          / \\
                |
            ----------
              ""","""
                -------------
                |           |
                |         __|__
                |         |___|   
                |           |
                |           |
                |          / \\
                |
            ----------
                ""","""
                -------------
                |           |
                |         __|__
                |         |___|   
                |           |
                |           |
                |           
                |
            ----------
            ""","""
                -------------
                |           |
                |         __|__
                |         |___|   
                |          
                |           
                |          
                |
            ----------
            
            """]
    return stages[tries]
def main():
    secret = get_word()
    play(secret)
    while input("Play again? (Y/N)").upper() == "Y":
        secret= get_word()
        play(secret)
if __name__ == "__main__":
    main()