# Project 2 - Spelling Bee 2.0, generate_puzzle.py (file 1 of 3)
# This code prompts the user to enter a 7 letter word. The word must be exactly 7 letters, have no repeating letters, and must contain no special characters
# If the requirements listed above are met, then the word that was input will be generated into the beehive
global letters, valid # do not change or add to


letters= input("Enter 7 puzzle letters: "  )
letters= letters.upper()
alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# check if word input is exactly 7 letters
if len(letters) != 7:
  valid = False
  print("Invalid puzzle, must enter exactly 7 letters.")
# Checks if word prompted has no repeating letters
else:
  duplicates1= letters.count(letters[0])
  duplicates2= letters.count(letters[1])
  duplicates3= letters.count(letters[2])
  duplicates4= letters.count(letters[4])
  duplicates5= letters.count(letters[5])
  duplicates6= letters.count(letters[6])
  if len(letters) == 7 and duplicates1 != 1:
    valid= False
    print("Invalid puzzle, must enter 7 unique letters.")
  elif len(letters) == 7 and duplicates2 != 1:
      valid= False
      print("Invalid puzzle, must enter 7 unique letters.")
  elif len(letters) == 7 and duplicates3 != 1:
      valid = False
      print("Invalid puzzle, must enter 7 unique letters.")
  elif len(letters) == 7 and duplicates4 != 1:
      valid = False
      print("Invalid puzzle, must enter 7 unique letters.")
  elif len(letters) == 7 and duplicates5 != 1:
      valid= False
      print("Invalid puzzle, must enter 7 unique letters.")
  elif len(letters) == 7 and duplicates6 != 1:
      valid= False
      print("Invalid puzzle, must enter 7 unique letters.")
# Check if word prompted contains no special characters
  else:
      if letters[0] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      elif letters[1] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      elif letters[2] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      elif letters[3] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      elif letters[4] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      elif letters[5] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      elif letters[6] not in alphabet:
          valid = False
          print("Invalid puzzle, must enter letters only (no numbers, symbols, etc.)")
      else:
          valid= True
          first_letter= letters[0]
          second_letter= letters[1]
          third_letter= letters[2]
          fourth_letter= letters[3]
          fifth_letter= letters[4]
          sixth_letter= letters[5]
          seventh_letter=letters[6]
          print("--------SPELLING BEE-------")
          print("--------- / ¯¯¯ \ ---------" )
          print("---------    {a}    ---------".format(a= third_letter))
          print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
          print("----   {b}           {c}   ----".format(b= fourth_letter, c= second_letter))
          print("----\ ___ / ¯¯¯ \ ___ / ----")
          print("---------    {d}    ---------".format(d= first_letter))
          print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
          print("----   {e}           {f}   ----".format(e= fifth_letter, f= seventh_letter))
          print("----\ ___ / ¯¯¯ \ ___ / ----")
          print("---------    {g}    ---------".format(g=sixth_letter))
          print("--------- \ ___ / ---------")

