# DO NOT EDIT THIS FILE - need to reset? go to starter code page.
##########################
# Project 1 - driver_MS2_1
# This file will call the student files:
# generate_puzzle.py
# play.py
# summary.py
# Author: Shanon Reckinger
# UIC, CS 111

global word, letters, dictionary, list, name, bonus

# The function returns True is the word is a valid solution for letters
# and will return False if it is not a valid word
def check_word(word, letters):
    set = {}
    for ch in word:
        if ch not in letters: # word must only contain beehive letters
            return False, 0
        else:
            set[ch] = ch
    if len(word) < 4: # word must be >= 4 characters
        return False, 0
    if letters[0] not in word: # word must contain middle letter
        return False, 0
    return True, len(set)

# This function make a dictionary.  They key is a word from the english
# dictionary and the value is the score for that word given letters.
# It adds all words from EnglishWords.txt.
def make_dict(letters):
    global bonus
    file = open("EnglishWords.txt")
    list_file = file.readlines()
    dictionary = {}
    for w in list_file:
        [test, ct] = check_word(w.strip(), letters.lower())  # Valid word
        if test:
            if len(w.strip()) == 4:
                dictionary[w.strip()] = 1
            elif ct == 7: # Bonus points if all 7 letters are used
                dictionary[w.strip()] = len(w.strip()) + 7
            else:
                dictionary[w.strip()] = len(w.strip())
        else: # Invalid word
            dictionary[w.strip()] = 0
    return dictionary

# Main code starts here
valid = False # get set to True once puzzle is properly generated
bonus = True # get sets to True if user plays a bonus word

# initialize some global variables
words_list = []
scores_list = []
first_time = True
letters=""

exec(open("generate_puzzle.py").read())
print("Your value for valid is: ", valid)
