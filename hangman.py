import random, os

def pa():
    playAgain = input("Do you want to play again? (y/n)")
    if playAgain.lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")
        play()
    if playAgain.lower() == "n":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Invalid input")
        pa()

def play():
    hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    words = []
    wordArray = []
    censoredWordArray = []
    letterIndex = 0
    word = ""
    tries = 0
    attempts = 7
    wordLength = 0
    guesses = 0
    wordFile = open("words.txt", "r")

    for x in wordFile:
        x.strip()
        words.append(x)
    wordFile.close()
    word = random.choice(words)
    words.clear()

    for char in word:
        wordArray.append(char)
        censoredWordArray.append("*")
        wordLength += 1
    del censoredWordArray[-1]
    del wordArray[-1]

    print("Word has: " + str(len(wordArray)) + " letters.")
    print(''.join(censoredWordArray))
    print(hangmanpics[0])
    
    while censoredWordArray != wordArray:
        
        guess = input(">")
        guesses += 1
        if len(guess) > 1 or len(guess) < 1:
            print("Invalid input")
        
        if len(guess) == 1:
            if guess in wordArray:
                if tries == 6:
                    break
                print("Correct")
                letterIndex = wordArray.index(guess)
                censoredWordArray[letterIndex] = guess
                if tries != 0:
                    print(hangmanpics[tries])
                print(''.join(censoredWordArray))
            if guess not in wordArray:
                tries += 1
                if tries == 6:
                    break
                print("Incorrect")
                print(hangmanpics[tries])
                print(''.join(censoredWordArray))

        print("Tries remaining: " + str(attempts - tries))
    if tries == 6:
        print(hangmanpics[6])
        print("You lose")
    else:
        print("You won in " + str(guesses) + " guesses.")
        if guesses == len(wordArray):
            print("Perfect game!")

play()
pa()