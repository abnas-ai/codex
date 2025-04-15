

# Write a program that asks the user some questions with the int() and input() functions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

# question = input("Do you like dawn or dusk? ").strip().lower()
# if question == "dawn":
#     print("You will go to Gryffindor and Ravendor")
# elif question == "dusk":
#     print("You will go to Hufflepuff or Slytherin")
# else:
#     print("Wrong input")
    
# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

#     If the answer is 1, Hufflepuff +2.
#     Else if answer is 2, Slytherin +2.
#     Else if answer is 3, Ravenclaw +2.
#     Else if answer is 4, Gryffindor +2.
#     Else, output the message "Wrong input."

# question = input("When i'm dead, i want people to remember me as: ")
# if question == "The Good":
#     print("Hufflepuff +2")
# elif question == "The Great":
#     print("Slytherin +2")
# elif question == "The Wise":
#     print("Ravenclaw +2")
# elif question == "The Bold":
#     print("Gryffindor +2")
# else:
#     print("Wrong input")
    
# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

#     If the answer is 1, Slytherin +4.
#     Else if the answer is 2, Hufflepuff +4.
#     Else if the answer is 3, Ravenclaw +4.
#     Else if the answer is 4, Gryffindor +4.
#     Else, output "Wrong input."

# Lastly, print out the score for each house.

question = input("Which kind of instrument most pleases your ear? ")
if question == "The Violin":
  print("Slythern +4")
elif question == "The Trumpet":
 print("Hufflepuff +4")
elif question == "The Piano":
 print(" Ravenclaw +4")
elif question == "The drum":
 print("Gryffindor +4")
else:
    print("wrong input")
    