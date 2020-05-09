import time
import random

word_list = ['MAVERICK', 'SMACK', 'BREAD', 'PYTHON', 'JAZZ', 'LOVABLE', 'MUSHROOM', 'SASQUATCH']
word = random.choice(word_list)
counter = 10
out_of_guesses = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess_container = []
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

'''Below is the function to call the initial set up and tell the player the rules'''


def beginning():
    print("You are playing Hangman!")
    time.sleep(1)
    print(f"The word is {str(len(word))} letters long.")
    time.sleep(1)
    print(f"Try to guess the word one letter at a time. If you guess wrong {str(counter)} times, it's game over!\n")
    time.sleep(2)


# use below functions to join guessed words together into one, depending on whether


def success_guess():
    guess_container.append(guess)
    word_so_far = "".join([x if x in guess_container else '_' for x in word])
    print(word_so_far)
    return word_so_far


def fail_guess():
    guess_container.append(guess)
    word_so_far = "".join([x if x in guess_container else '_' for x in word])
    print(word_so_far)
    print(f"Attempts left: {str(counter)}")
    return word_so_far


def hangman_combo():
    if counter in range(10):
        print(hangman_art.get(counter))


beginning()

# main game loop below

while True:
    if counter == 0:   # this is necessary up here because otherwise, if it is simply attached as an else statement
        out_of_guesses = True  # below, the program will allow one to guess when the counter = 0
        break

    guess = input("Guess a letter: ").upper()

    if guess not in alphabet:  # catch exceptions
        print("Please enter only a single letter from A-Z")
        continue

    if guess in guess_container and guess not in word:
        print("You have already used that letter! Try another one")
        counter -= 1
        hangman_combo()
        print(f"Attempts left: {str(counter)}")
        continue

    if guess not in word and not out_of_guesses:
        if counter > 0:
            counter -= 1
            print("Not quite")
            hangman_combo()
            fail_guess()
            continue

    elif guess in word and not out_of_guesses:
        print(f"Good job, {guess} is in the word")
        word_so_far = success_guess()
        if word == word_so_far:
            success = True
            break
        else:
            continue

# end conditions

if out_of_guesses:
    time.sleep(1)
    print("You are out of guesses \nGame Over")

if success:
    time.sleep(1)
    print("Congratulations! \nYOU WIN")
