import time
import random

word_list = ['MAVERICK', 'SMACK', 'BREAD', 'PYTHON', 'JAZZ', 'LOVABLE', 'MUSHROOM', 'SASQUATCH']   # use list
word = random.choice(word_list)  # select a word at random from the list
counter = 10  # number of guesses user has to get it right
out_of_guesses = False  # set variable to FALSE so once it is true, it triggers the end condition
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # list of possible letters
guess_container = []  # container to hold guessed letters
word_so_far = ["_"] * len(word)  # make place holder to display guessed letters be equal to the length of the word
success = False  # set to FALSE so once it is true, it triggers win condition
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
_____________''')  # use tuples so they are immutable and print in that order
hangman_art = {0: Dead1, 1: Dead2, 2: Dead3, 3: Dead4, 4: Dead5, 5: Dead6, 6: Dead7, 7: Dead8,
               8: Dead9, 9: Dead10}   # use a dictionary, set the key to the counter, set the value to a word so we can
                                        # print the art without having to type out the whole thing
'''Below is the function to call the initial set up and tell the player the rules'''


def beginning():
    print("You are playing Hangman!")
    time.sleep(1)
    print("The word is", str(len(word)), "letters long.")
    time.sleep(1)
    print("Try to guess the word one letter at a time. If you guess wrong " + str(counter) + " times, it's game over!\n")
    time.sleep(2)


# use below function to join guessed words together into one


def guessing():
    global success  # use global variables to connect the function and the main game loop
    global guess_container
    guess_container.append(guess)  # append the guessed letters to the word, creating a list that contains them, like [s, p, t] so when a letter is guessed twice the player is informed
    word_so_far = "".join([x if x in guess_container else '_' for x in word])  # when the player guesses a letter (referred to here as 'x') that is in the word, it is joined to the word as itself and displayed as part of guess_container; if the letter has already been guessed, it is printed as '_', just like in the original word_so_far
    if guess in word:   # if the guess is in the word, print the word_so_far, like S___K
        print(word_so_far)
        if word_so_far == word:
            success = True
    else:
        print("".join(word_so_far))  # if the guess is not in the word, we join it like above anyway
        print("Attempts left: " + str(counter))  # tell player how many attempts left there are


# use the below function to print hangman art when a wrong letter is guessed


def hangman_combo():
    if counter in range(10):  # when counter corresponds to appropriate hangman pic, print it
        print(hangman_art.get(counter))


beginning()

# main game loop below

while True:  # use a while loop to repeat until conditions are met
    if success:  # place end conditions at top, so if it has been met it is hit first as Python cycles through loop
        break
    if counter == 0:   # this is necessary up here because otherwise, if it is simply attached as an else statement
        out_of_guesses = True  # below line 182, the program will allow one to guess when the counter = 0
        break

    guess = input("Guess a letter: ").upper()  # ask user for a letter, make it uppercase so it fits with our alphabet

    if guess not in alphabet:  # catch exceptions
        print("Please enter only a single letter from A-Z")
        continue

    if guess in guess_container and guess not in word:  # if user guessed previously used word, they are penalized
        print("You have already used that letter! Try another one")
        counter -= 1
        hangman_combo()  # print pics only when they get one wrong; see section below as well
        print("Attempts left: " + str(counter))
        continue

    if guess not in word and not out_of_guesses:  # guessing() will be called during different times; it will be the
        if counter > 0:                           # same function no matter which statement it is called from, but that
            counter -= 1                          # is fine because guessing() contains within itself ways to
            print("Not quite")                    # differentiate what will happen depending on the guess
            hangman_combo()
            guessing()
            continue

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
