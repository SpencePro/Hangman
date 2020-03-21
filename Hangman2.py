import time
import random

word_list = ['MAVERICK', 'SMACK', 'BREAD', 'PYTHON', 'JAZZ', 'LOVABLE', 'MUSHROOM', 'SASQUATCH']
word = random.choice(word_list)
guess = "`"
counter = 10  # number of guesses user has to get it right
out_of_guesses = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess_container = []  # container to hold guessed letters
word_so_far = ["_"] * len(word)  # make place holder to display guessed letters be equal to the length of the word
success = False
Dead1 = ('''    
     _______
     |   \ |
   (x_x)  \|
     |     |
   / | \  /|
    / \  / |
        /  |
_______/___|_
_____________''')
Dead2 = ('''    
     _______
     |   \ |
   (   )  \|
     |     |
   / | \  /|
    / \  / |
        /  |
_______/___|_
_____________''')
Dead3 = ('''    
     _______
     |   \ |
   (   )  \|
     |     |
   / | \  /|
    /    / |
        /  |
_______/___|_
_____________''')
Dead4 = ('''    
     _______
     |   \ |
   (   )  \|
     |     |
   / | \  /|
         / |
        /  |
_______/___|_
_____________''')
Dead5 = ('''    
     _______
     |   \ |
   (   )  \|
     |     |
   / |    /|
         / |
        /  |
_______/___|_
_____________''')
Dead6 = ('''    
     _______
     |   \ |
   (   )  \|
     |     |
     |    /|
         / |
        /  |
_______/___|_
_____________''')
Dead7 = ('''    
     _______
     |   \ |
   (   )  \|
     |     |
          /|
         / |
        /  |
_______/___|_
_____________''')
Dead8 = ('''    
     _______
     |   \ |
   (   )  \|
           |
          /|
         / |
        /  |
_______/___|_
_____________''')
Dead9 = ('''    
     _______
     |   \ |
          \|
           |
          /|
         / |
        /  |
_______/___|_
_____________''')
Dead10 = ('''    
     _______
         \ |
          \|
           |
          /|
         / |
        /  |
_______/___|_
_____________''')
hangman_art = {0: Dead1, 1: Dead2, 2: Dead3, 3: Dead4, 4: Dead5, 5: Dead6, 6: Dead7, 7: Dead8,
               8: Dead9, 9: Dead10}


def beginning():
    print("You are playing Hangman!")
    # time.sleep(1)
    print("The word is", str(len(word)), "letters long.")
    # time.sleep(1)
    print(
        "Try to guess the word one letter at a time. If you guess wrong " + str(counter) + " times, it's game over!\n")
    # time.sleep(2)


def guessing():
    global success
    global guess_container
    guess_container.append(guess)
    word_so_far = "".join([x if x in guess_container else '_' for x in word])
    if guess in word:
        print(word_so_far)
        if word_so_far == word:  # if the word has been guessed, end loop
            success = True
    else:
        print("".join(word_so_far))
        print("Attempts left: " + str(counter))


# use above function to join guessed words together into one


def hangman_combo():
    if counter in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(hangman_art.get(counter))


beginning()

# main game loop below

while True:
    if success:
        break
    if counter == 0:
        out_of_guesses = True
        break

    guess = input("Guess a letter: ").upper()

    if guess not in alphabet and guess != "`":
        print("Please enter only a single letter from A-Z")
        continue

    if guess in guess_container and guess not in word:
        print("You have already used that letter! Try another one")
        counter -= 1
        hangman_combo()
        print("Attempts left: " + str(counter))
        continue

    if guess not in word and not out_of_guesses:
        if counter > 0:
            counter -= 1
            print("Not quite. Enter another letter")
            hangman_combo()
            guessing()
            continue
        else:
            out_of_guesses = True
            break

    elif guess in word and not out_of_guesses:
        print("Good job, " + guess + " is in the word:")
        guessing()
        continue

# end conditions

if out_of_guesses:
    time.sleep(1)
    print("You are out of guesses \nGame Over")

if success:
    time.sleep(1)
    print("Congratulations! \nYOU WIN")
