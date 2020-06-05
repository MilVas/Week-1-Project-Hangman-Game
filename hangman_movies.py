import random
import string

movies = ["star wars", "clockwork orange", "the conversation", "vertigo", "the godfather", "goodfellas", "taxi driver", 
"lawrence of arabia","dressed to kill", "easy rider", "bonnie and clyde", "the deer hunter", "blade runner" ]


def start(): 
    print("     ")
    print("     ")
    print("     ")
    print("...........GUESS THE NAME OF A MOVIE................")
    print("                                                    ")
    print("     ")
    print("     ")
    print("Do you want to play?")
    choice = input("Please enter 'yes' or 'no'   ")
    if choice == "yes":
        play()
    elif choice == "no":
        print("Too bad, bye")
        exit()
    elif choice != "yes" or choice != "no":
        print(" You can only choose yes or no. Please try again.")
    return choice
    
def play():
    word = random.choice(movies)
    spaces = ['_'] * len(word) #- word.count(" "))
    attempt = 6
    for n, i in enumerate(word):
        if i == " " :
            spaces[n] = " "
    while '_' in spaces and attempt > 0:
        print(' '.join(spaces))
        print("    ")
        character = input('Enter character: ')

        if len(character) > 1:
            print("   ")
            print('Only enter one character.')
            continue

        if character not in list(string.ascii_lowercase):
            print("You can only choose a-z letters.")
            print("   ")
            continue

        if character not in word :
            attempt -= 1
            print('Wrong! You have', attempt, 'attempts left.')
            print(" ")
        
        for i, j in enumerate(word):
            if j == character:
                    spaces[i] = character

        if attempt == 0:
            print('You lose! The right movie was', word)
            print(" ")
            attempt = 6
            start()
    
    if "_" not in spaces:
            print("You won! The movie is", word, ".")
            start() 




start()

