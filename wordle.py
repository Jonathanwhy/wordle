import random

possible_words= ["tired","water","brown","broke","truck","crash","brass","child","puppy","green","apple","mango"]
word = random.choice(possible_words)

green = '\033[92m'
yellow = '\033[33m'
default = '\033[0m'

def hint(guess):

    color = default
    hint = ''

    for i in range(5):
        if (guess[i]==word[i]):
            color=green
        elif (guess[i] in word):
            color=yellow
        else:
            color = default
        hint = hint + color + guess[i]+ default

    return hint

def guesses():
    guess = ''
    for i in range(6):
        guess = input("What is your guess?:")
        if guess == word:
            print("You got it!")
            break
        else:
            print(hint(guess))

guesses()


