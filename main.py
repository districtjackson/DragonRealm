import random
import time


def display_intro():
    print('''You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.''')


def choose_cave():
    cave = ''

    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def check_cave(playerChoice):
    print('You approach the cave...')
    print('It is large and spooky...')
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(2)

    if playerChoice == str(random.randint(1, 2)):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")


playing = True

while playing:
    display_intro()
    check_cave(choose_cave())

    playAgain = ''

    while playAgain != "yes" and playAgain != 'no':
        print("Do you want to play again?")
        playAgain = input()

    if playAgain == 'no':
        playing = False
