
# # Write a program that asks the user some questions with the int() and input() functions:

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


# *************SOLUTION******
# Ask the question
question = input("Q1) Do you like Dawn or Dusk?\n  1) Dawn\n  2) Dusk\nYour answer: ").strip().lower()

# Evaluate the answer
if question == "dawn" or question == "1":
    print("You will go to Gryffindor and Ravendor")
elif question == "dusk" or question == "2":
    print("You will go to Hufflepuff or Slytherin")
else:
    print("Wrong input.")


    
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

# *************SOLUTION******
# Initialize house points
slytherin = 0
hufflepuff = 0
ravenclaw = 0
gryffindor = 0

# Display the question
print("Q2) When I’m dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")

# Get user input
answer = input("Enter the number of your choice: ")

# Evaluate the answer
if answer == "1":
    hufflepuff += 2
elif answer == "2":
    slytherin += 2
elif answer == "3":
    ravenclaw += 2
elif answer == "4":
    gryffindor += 2
else:
    print("Wrong input.")

# # Optional: Print house points (for verification)
# print("Slytherin:", slytherin)
# print("Hufflepuff:", hufflepuff)
# print("Ravenclaw:", ravenclaw)
# print("Gryffindor:", gryffindor)


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

# ***************SOLUTION******
# Initialize house points
slytherin = 0
hufflepuff = 0
ravenclaw = 0
gryffindor = 0

# Display the question
print("Q3) Which kind of instrument most pleases your ear?")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")

# Get user input
answer = input("Enter the number of your choice: ")

# Evaluate the answer
if answer == "1":
    print("slytherin +4")
elif answer == "2":
    print("hufflepuff +4")
elif answer == "3":
    print("ravenclaw +4")
elif answer == "4":
    print("gryffindor +4")
else:
    print("Wrong input.")

# Optional: Print house points (for verification)
# print("Slytherin:", slytherin)
# print("Hufflepuff:", hufflepuff)
# print("Ravenclaw:", ravenclaw)
# print("Gryffindor:", gryffindor)

# ****Lastly, print out the score for each house.***
#   *******SOLUTION************

max_points = max(gryffindor, hufflepuff, ravenclaw, slytherin)
print("\nYou belong to...")

if gryffindor == max_points:
    print("Gryffindor!")
elif hufflepuff == max_points:
    print("Hufflepuff!")
elif ravenclaw == max_points:
    print("Ravenclaw!")
elif slytherin == max_points:
    print("Slytherin!")


# ******LONG METHOD*************
# Initialize house points
# slytherin = 0
# hufflepuff = 0
# ravenclaw = 0
# gryffindor = 0

# # --- Q1 ---
# print("Q1) Do you like Dawn or Dusk?")
# print("  1) Dawn")
# print("  2) Dusk")
# answer1 = input("Your answer: ").strip().lower()

# if answer1 == "1" or answer1 == "dawn":
#     gryffindor += 1
#     ravenclaw += 1
#     print("Gryffindor +1, Ravenclaw +1")
# elif answer1 == "2" or answer1 == "dusk":
#     hufflepuff += 1
#     slytherin += 1
#     print("Hufflepuff +1, Slytherin +1")
# else:
#     print("Wrong input.")

# # --- Q2 ---
# print("\nQ2) When I’m dead, I want people to remember me as:")
# print("  1) The Good")
# print("  2) The Great")
# print("  3) The Wise")
# print("  4) The Bold")
# answer2 = input("Your answer: ").strip()

# if answer2 == "1":
#     hufflepuff += 2
#     print("Hufflepuff +2")
# elif answer2 == "2":
#     slytherin += 2
#     print("Slytherin +2")
# elif answer2 == "3":
#     ravenclaw += 2
#     print("Ravenclaw +2")
# elif answer2 == "4":
#     gryffindor += 2
#     print("Gryffindor +2")
# else:
#     print("Wrong input.")

# # --- Q3 ---
# print("\nQ3) Which kind of instrument most pleases your ear?")
# print("  1) The violin")
# print("  2) The trumpet")
# print("  3) The piano")
# print("  4) The drum")
# answer3 = input("Your answer: ").strip()

# if answer3 == "1":
#     slytherin += 4
#     print("Slytherin +4")
# elif answer3 == "2":
#     hufflepuff += 4
#     print("Hufflepuff +4")
# elif answer3 == "3":
#     ravenclaw += 4
#     print("Ravenclaw +4")
# elif answer3 == "4":
#     gryffindor += 4
#     print("Gryffindor +4")
# else:
#     print("Wrong input.")

# # --- Final Scores ---
# print("\nFinal House Points:")
# print("Gryffindor:", gryffindor)
# print("Hufflepuff:", hufflepuff)
# print("Ravenclaw:", ravenclaw)
# print("Slytherin:", slytherin)

# # --- Optional: Sorting Result ---
# max_points = max(gryffindor, hufflepuff, ravenclaw, slytherin)
# print("\nYou belong to...")

# if gryffindor == max_points:
#     print("Gryffindor!")
# elif hufflepuff == max_points:
#     print("Hufflepuff!")
# elif ravenclaw == max_points:
#     print("Ravenclaw!")
# elif slytherin == max_points:
#     print("Slytherin!")

