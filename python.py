def get_tof_questions():
        questions = []
        questions (["April 15th is the last day to send in Federal Income Tax Forms","T"])
        questions (["Jimmy Carter was the 39th President", "T"])
        questions (["There are 28 amendments", "F" ])
        questions (["Speech, Religion, assembly, press, and labor are apart of the First Amendment", "F"])
        questions (["The cabinents are in charge of federal laws", "F" ])
        questions (["Pub;ius was one of the writers on the U.S. Constitution", "T"])

        return questions

        def play_tof_quiz():
        # Get true of false statements
        tof_questions = get_tof_questions()
# Set player score to 0
    score=0
# Show tof questions using a loop
for q in tof_questions:

  # Present statement
  print("True or false: " + s[0] )
  # user enter guess
    guess= input("Enter T or F:")
  # check if guess is correct
  if guess == s[1]:
      print("Correct!")
    # update score
score=score + 1
else:
    print("Incorrect :( ")
# Show final score
print("Your final score is:" + str(score))

def main_menu():

    print("+---------------------+")
    print(" WELCOME TO US TRUE OR FALSE ")
    print("+---------------------+")
    print(" PLEASE SELECT AN OPTION ")
    print("                   ")
    print( "1. Play True or False Quiz" )
    print(" 0. Quit" )
    print("+---------------------+")

    choice = input("Enter 1 or 0")
    if choice =="1"
        play_tof_quiz
    elif choice == 0:
        print("Thanks for playing! :) ")
        quit()

main_menu()
