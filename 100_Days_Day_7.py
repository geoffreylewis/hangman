###########
# Hangman #
###########

# Importing module.
import random

# ASCII art for the hanged man.
hanged_man_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Counter for number of body parts that appear before the stick figure man is hung.
number_of_body_parts = 0

# Counter for different ASCII images of the hanged man.
hanged_man_stage_number = 6

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
print(selected_word) # TESTING CODE

# Empty list for eventual "_" characters.
hidden_word_underscores = []
for char in selected_word:
    hidden_word_underscores.append("_")
print(hidden_word_underscores) # TESTING CODE

# Guessing letters.
while "_" in hidden_word_underscores and number_of_body_parts < 6:
    print(hanged_man_stages[hanged_man_stage_number])
    player_guess = str(input("Guess a letter: ").lower())
    letter_position = 0 # Starting position in hidden word list.
    for letter in selected_word: # Analyzes player's guess against the selected word.
        if player_guess == letter:
            print("Right") # TESTING CODE
            hidden_word_underscores[letter_position] = letter
            letter_position += 1
        else:
            letter_position += 1
            print("Wrong") # TESTING CODE
    if player_guess not in selected_word: # Appearance of body parts / wrong guesses.
        number_of_body_parts += 1
        hanged_man_stage_number -= 1
    print(hidden_word_underscores) # TESTING CODE

# End of project.
if "_" not in hidden_word_underscores and number_of_body_parts < 6:
    print("You win!  You saved your stick figure man!")
else:
    print(hanged_man_stages[0])
    print("You lose!  You're too late and didn't save your stick figure man!")