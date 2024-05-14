###########
# Hangman #
###########

# Importing module.
import random

# ASCII art for beginning banner/logo (courtesy of https://replit.com/@appbrewery/Day-7-Hangman-5-Start#hangman_art.py).
banner_logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# ASCII art for the hanged man (courtesy of https://replit.com/@appbrewery/Day-7-Hangman-5-Start#hangman_art.py).
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

# Beginning of game.
print(banner_logo)
print()
print("Welcome to the \"Hangman\" game!\n")
print("You have to guess the mystery word one letter at a time.\n")
print("If you guess wrong 6 times before revealing the full word, your stick figure man is hanged on the gallows.\n")
print("Don't guess wrong, or it will be too late for your stick figure man!\n")

# Counter for number of body parts that appear before the stick figure man is hung.
number_of_body_parts = 0

# Counter for different ASCII images of the hanged man.
hanged_man_stage_number = 6

# Word list to pick a random word from.
list_of_words = ["abruptly", "absurd", "abyss", "avenue", "awkward", "bagpipes", "bandwagon", "banjo", "bayou", 
                 "bikini", "bookworm", "chicken", "crypt", "dwarves", "embezzle", "funny", "galvanize", "goblins", "glyph", "hyphen", 
                 "ivory", "jigsaw", "keyhole", "lucky", "matrix", "monkey", "nymph", "onyx", "phlegm", "quips", "rhythm", "royalty", 
                 "steak", "swivel", "trolls", "topaz", "uptown", "vampire", "vaporize", "wellspring", "werewolf", "xylophone", 
                 "yesterday", "yummy", "zebra", "zombie"]

# Random word from the list is selected.
selected_word = random.choice(list_of_words)

# Empty list for eventual "_" characters.
hidden_word_underscores = []
for char in selected_word:
    hidden_word_underscores.append("_")
print(hidden_word_underscores)

# Empty list for already-guessed letters.
already_guessed = []

# Guessing letters.
while "_" in hidden_word_underscores and number_of_body_parts < 6:
    print(hanged_man_stages[hanged_man_stage_number])
    player_guess = str(input("Guess a letter: ").lower())
    letter_position = 0 # Starting position in hidden word list.
    for letter in selected_word: # Analyzes player's guess against the selected word.
        if player_guess == letter:
            hidden_word_underscores[letter_position] = letter
            letter_position += 1
        else:
            letter_position += 1
    if player_guess not in selected_word: # Appearance of body parts / wrong guesses.
        if player_guess not in already_guessed:
            already_guessed.append(player_guess)
            number_of_body_parts += 1
            hanged_man_stage_number -= 1
            print()
            print(f"Letter \"{player_guess}\" isn't in the word.  Your stick figure man is getting closer to death.\n")
            print("Tread lightly.")
        elif player_guess in already_guessed:
            print()
            print("You already guessed this letter; pick a different one.")
    elif player_guess in selected_word:
        if player_guess not in already_guessed:
            already_guessed.append(player_guess)
        elif player_guess in already_guessed:
            print()
            print("You already guessed this letter; pick a different one.")
    print()
    print(hidden_word_underscores)

# End of game.
if "_" not in hidden_word_underscores and number_of_body_parts < 6:
    print()
    print(f"You win!  The word was \"{selected_word}\".  You saved your stick figure man from the gallows!")
else:
    print(hanged_man_stages[0])
    print(f"You lose!  The word was \"{selected_word}\".  You're too late and didn't save your stick figure man!")