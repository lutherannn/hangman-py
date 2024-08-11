import os
import time
import random


def getWord():
    with open("words.txt", "r") as f:
        return random.choice(f.readlines()).strip()


wordToGuess = getWord()
guesses = 0
correctGuesses = 0
guessesNeeded = len(set(wordToGuess))
guessedLetters = []

while correctGuesses < guessesNeeded:
    print(wordToGuess)
    print("".join([x if x in guessedLetters else "*" for x in wordToGuess]))
    print(f"Guessed Letters: {" ".join(guessedLetters)}")
    print(f"Guesses: {guesses}")
    guess = input("Enter letter to guess: ")
    if guess in guessedLetters:
        print("Letter already gussed.")
        time.sleep(1)
    if guess not in guessedLetters:
        guesses += 1
        guessedLetters.append(guess)
        if guess in wordToGuess:
            correctGuesses += 1

    os.system("cls" if os.name == "nt" else "clear")

print(f"You guessed the word \"{wordToGuess}\" in {guesses} guesses")
