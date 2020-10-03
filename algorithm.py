import random
import re

wordslist = ["PESCE PALLA"]


def FindIndex(letter, string):
    return [x.start() for x in re.finditer(letter, string)]


def Swap(hiddenword, letter, i):
    hiddenword = list(hiddenword)
    hiddenword[i] = (letter)
    return "".join(hiddenword)


word = random.choice(wordslist)
hiddenword = "-" * len(word)
tries = 5
if " " in word:
    for i in FindIndex(" ", word):
        hiddenword = Swap(hiddenword, " ", i)

print("You only have 5 tires for this game")
print("Insert 1 if you want to write a letter, 2 if you want to try writing the word")
while tries != 0:
    comand = int(input())
    if comand == 1:
        letter = str(input()).upper()
        if letter in word:
            for i in FindIndex(letter, word):
                hiddenword = Swap(hiddenword, letter, i)

        else:
            print("WRONG")
            tries -= 1
            print("You have %i tries" % tries)
            print(hiddenword)

        if hiddenword == word:
            break
    if comand != 1 or comand != 2:
        print("Insert 1 if you want to write a letter, 2 if you want to try writing the word")

    if comand == 2:
        UserWord = str(input()).upper()
        if UserWord == word:
            break
        else:
            print("WRONG")
            tries -= 1
            print("You have %i tries" % tries)
            print(hiddenword)
    print(hiddenword)
print("CONGRATULATIONS")
print("The word was %s" %word)
