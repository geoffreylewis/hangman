###########
# Hangman #
###########

# Importing module.
import random

# Beginning of game.
print("Welcome to the \"Hangman\" game!")
print("You have to guess the mystery word one letter at a time.")
print("If you guess wrong 6 times before revealing the full word, your stick figure man is hanged on the gallows.")
print("Don't guess wrong, or it will be too late for your stick figure man!")

# Word list to pick a random word from.
list_of_words = ["abruptly", "absurd", "abyss", "avenue", "awkward", "bagpipes", "bandwagon", "banjo", "bayou", 
                 "bikini", "bookworm", "crypt", "dwarves", "embezzle", "funny", "galvanize", "glyph", "hyphen", 
                 "ivory", "jigsaw", "keyhole", "lucky", "matrix", "nymph", "onyx", "phlegm", "quips", "rhythm", 
                 "swivel", "topaz", "uptown", "vampire", "vaporize", "wellspring", "werewolf", "xylophone", 
                 "yummy", "zombie"]

# Random word from the list is selected.
selected_word = random.choice(list_of_words)
print(selected_word)

# Guessing letters.
player_guess = input("Guess a letter: ")
for letter in selected_word:
    if player_guess == letter:
        print("Right")
    else:
        print("Wrong")

# End of project.
print("You win!  You saved your stick figure man!")