import random

words = []
wordArray = []
censoredWordArray = []
letterIndex = 0
word = ""
guesses = 0
tries = 10
wordLength = 0

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
while censoredWordArray != wordArray:
    guess = input(">")
    
    if len(guess) > 1 or len(guess) < 1:
        print("Invalid input")
    
    if len(guess) == 1:
        guesses += 1
        if guess in wordArray:
            print("Correct")
            letterIndex = wordArray.index(guess)
            censoredWordArray[letterIndex] = guess
            print(''.join(censoredWordArray))
        if guess not in wordArray:
            print("Incorrect")
            tries -= 1
            print(''.join(censoredWordArray))
        if tries == 0:
            print("You lose.")
            print("The word was: " + word)
            break
    print("Tries remaining: " + str(tries))

if tries > 0:
    print("You won in " + str(guesses) + " guesses.")
    if guesses == len(wordArray):
        print("Perfect game!")