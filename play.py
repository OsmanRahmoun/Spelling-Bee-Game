# Project 2 - Spelling Bee 2.0, play.py (file 2 of 3)

global letters, dictionary, word, score, words_list, scores_list # do not change or add to
# This section asks the player to input different word guesses of the beehive word, the word prompted is checked to make sure that it is 4 or more letters, contains the middle beehive letters, and is a word within the dictionary. If the word prompted fails 1 or more of these rules, than they will be giving a message explaining their error

mixed_words= input("Word: ")
words= mixed_words.lower()
#checks if word is in dictionary 
if words in dictionary:
#checks if word contains 4 letters and has the middle beehive letter (multiple mistakes)
  if (len(words) <= 3) and letters[0] not in words.upper():
    score= 0
    print("Score for {a}: {b}".format(a= mixed_words, b= score))
    print("{a} contains less than 4 letters so no points given.".format(a= mixed_words))
    print("{a} does not contain the middle letter, {b} so no points given.".format(a= mixed_words, b= letters[0]))
    words_list += [mixed_words]
    scores_List = scores_list.append(score)
#checks if word contains atleast 4 letters
  elif len(words) <= 3:
    score= 0
    print("Score for {a}: {b}".format(a= mixed_words, b= score))
    print("{a} contains less than 4 letters so no points given.".format(a= mixed_words))
    words_list += [mixed_words]
    scores_List= scores_list.append(score)
#checks if word has middle beehive letter
  elif letters[0] not in words.upper():
    score= 0
    print("Score for {a}: {b}".format(a= mixed_words, b= score))
    print("{a} does not contain the middle letter, {b} so no points given.".format(a= mixed_words, b= letters[0]))
    words_list += [mixed_words]
    scores_List= scores_list.append(score)
  else:
    score = dictionary[str(words)]
    print("Score for {a}: {b}".format(a= mixed_words, b= score)) 
    words_list += [mixed_words]
    scores_List= scores_list.append(score)
#if word is not in the dictionary
elif words not in dictionary:
  score = 0
  print("Score for {a}: {b}".format(a= mixed_words, b= score))
  print("{a} is not in the dictionary so no points given.".format (a= mixed_words))
  words_list += [mixed_words]
  scores_List= scores_list.append(score)
