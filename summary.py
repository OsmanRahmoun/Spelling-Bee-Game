# Project 1 - Spelling Bee 2.0, summary.py (file 3 of 3)

global name, words_list, scores_list, bonus # do not change or add to

#This code displays whether the player has one the game or not, lets them know the scores of each of their words and displays the word, and tells them if they scored a bonus

scores_sum= scores_list[0] + scores_list[1] + scores_list[2] + scores_list[3] + scores_list[4] + scores_list[5]

#If player scores atleast 1 point on each word (Meaning they win)
if scores_list[0] and scores_list[1] and scores_list[3] and scores_list[4] and scores_list[5] > 0:
  print("************************\nGAME OVER\n************************")
  print("You win, " + name + "!")
  print("Final Score:", scores_sum)
  print("Words played:")
  print(words_list[0]+"("+str(scores_list[0])+")")
  print(words_list[1]+"("+str(scores_list[1])+")")
  print(words_list[2]+"("+str(scores_list[2])+")")
  print(words_list[3]+"("+str(scores_list[3])+")")
  print(words_list[4]+"("+str(scores_list[4])+")")
  print(words_list[5]+"("+str(scores_list[5])+")")
#If the player does not score atleast 1 point on each word (Meaning they lost)
else:
  print("************************\nGAME OVER\n************************")
  print("You lost, " + name + "!")
  print("Final Score:", scores_sum)
  print("Words played:")
  print(words_list[0]+"("+str(scores_list[0])+")")
  print(words_list[1]+"("+str(scores_list[1])+")")
  print(words_list[2]+"("+str(scores_list[2])+")")
  print(words_list[3]+"("+str(scores_list[3])+")")
  print(words_list[4]+"("+str(scores_list[4])+")")
  print(words_list[5]+"("+str(scores_list[5])+")") 

#if bonus word was found:
if bonus:
  print("Congrats on finding a bonus word!")

