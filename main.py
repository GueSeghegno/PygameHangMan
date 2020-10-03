import pygame
import re
import random

pygame.init()
pygame.display.set_caption("HangMan")
icon = pygame.image.load("hang.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1080, 720))

running = True
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Z"]


class Button():
    def __init__(self, color, x, y, radious, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.radious = radious
        self.text = text

    def Draw(self, screen, outline=True):
        if outline:
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radious + 1, 0)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radious, 0)
        if self.text != "":
            font = pygame.font.Font("freesansbold.ttf", 30)
            text = font.render(self.text, True, (255, 255, 255))
            screen.blit(text, (self.x - 11, self.y - 13))

    def IsOver(self, pos):
        if pos[0] > self.x - 40 and pos[0] < self.x + self.radious:
            if pos[1] > self.y - 40 and pos[1] < self.y + self.radious:
                return True
        return False


def Swap(hiddenword, letter, i):
    hiddenword = list(hiddenword)
    hiddenword[i] = letter
    return "".join(hiddenword)


def FindIndex(letter, string):
    return [x.start() for x in re.finditer(letter, string)]


def Show_Word(word, x, y, big):
    font = pygame.font.Font("freesansbold.ttf", big)
    ScreenWord = font.render(str(word), True, (255, 255, 255))  # before blint you need to render
    # text you want, True, color
    screen.blit(ScreenWord, (x, y))


buttons = []
x = 50

wordslist = ["PAROLA STACCATA", "CANE", "VECCHIO", "ASTRONAVE", "MACCHINA", "ENCICLOPEDIA", "CARTA VETRATA"]
word = random.choice(wordslist)
hiddenword = "-" * len(word)

tries = 5
if " " in word:
    for i in FindIndex(" ", word):
        hiddenword = Swap(hiddenword, " ", i)

for j in letters[0:7]:
    buttons.append(Button((0, 40, 200), x, 50, 40, j))
    x += 162
x = 50
for j in letters[7:14]:
    buttons.append(Button((0, 40, 200), x, 150, 40, j))
    x += 162
x = 50
for j in letters[14:]:
    buttons.append(Button((0, 40, 200), x, 250, 40, j))
    x += 162

hangman0 = pygame.image.load("hangman0.png")
hangman1 = pygame.image.load("hangman1.png")
hangman2 = pygame.image.load("hangman2.png")
hangman3 = pygame.image.load("hangman3.png")
hangman4 = pygame.image.load("hangman4.png")
hangman5 = pygame.image.load("hangman5.png")
hangman6 = pygame.image.load("hangman6.png")
tries = [hangman1, hangman2, hangman3, hangman4, hangman5, hangman6]
print(hiddenword)
a = -1
while running:
    pos = pygame.mouse.get_pos()
    screen.fill((155, 40, 90))
    screen.blit(hangman0, (450, 400))
    Show_Word(hiddenword, 250, 650, 70)
    for i in buttons:
        i.Draw(screen, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.MOUSEMOTION:
                for i in range(0, 21):
                    if buttons[i].IsOver(pos):
                        buttons[i].color = (0, 255, 0)
                else:
                    buttons[i].color = (0, 40, 200)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, 21):
                if buttons[i].IsOver(pos):
                    letter = letters[buttons.index(buttons[i])]
                    if letter in word:
                        for i in FindIndex(letter, word):
                            hiddenword = Swap(hiddenword, letter, i, )
                    else:
                        a += 1
                        hangman0 = tries[a]
    if a == 5:
        Show_Word("HAI PERSO", 400, 340, 40)
    if hiddenword == word:
        Show_Word("HAI VINTO", 400, 340, 40)

    pygame.display.update()
