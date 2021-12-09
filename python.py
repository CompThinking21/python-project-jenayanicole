def play_tof_quiz():
# Get true of false statements
def get_tof_questions():
        questions=[]
        questions (["April 15th is the last day to send in Federal Income Tax Forms","T"])
        questions (["Jimmy Carter was the 39th President", "T"])
        questions (["There are 28 amendments", "F" ])
        questions (["Speech, Religion, assembly, press, and labor are apart of the First Amendment" ])
        questions (["The cabinents are in charge of federal laws")
        questions (["Pub;ius was one of the writers on the U.S. Constitution"])

        return questions
        answers
def ans_tof_qustions():
    answers=[]
    s[0]("T")
    s[1]("T")
    s[2]("F")
    s[3]("F")
    s[4]("F")
    s[5]("T")
# Set player score to 0
    player_score()=0
# Show tof questions using a loop
for q in tof_questions:
  # Present statement
  print("True or false: " + s[0] )
  print("True or false: " + s[1] )
  print("True or false: " + s[2] )
  print("True or false: " + s[3] )
  print("True or false: " + s[4] )
  print("True or false: " + s[5] )
  # user enter guess
    guess()= input("Enter T or F:")
  # check if guess is correct
  if guess == s[0]:
      print("Correct!")
    # update score
    player_score()= 0 + 1
else:
    print("Incorrect :( ")
 if guess == s[1]:
         print("Correct!")
       # update score
   player_score()= 0 + 1
   else:
       print("Incorrect :( ")
 if guess == s[2]:
     print("Correct!")
   # update score
   player_score()= 0 + 1
else:
   print("Incorrect :( ")
   if guess == s[3]:
       print("Correct!")
     # update score
     player_score()= 0 + 1
 else:
     print("Incorrect :( ")
     if guess == s[4]:
         print("Correct!")
       # update score
      player_score()= 0 + 1
   else:
       print("Incorrect :( ")
# Show final score
print("Your final score is:" + str(score))
def main_menu():
#main menu
    print("+---------------------+")
    print(" WELCOME TO ARE YOU EVEN AMERICAN DUDE? ")
    print("The purpose of this quiz is to test if you are even American DUDE?! How well do you know your home lands history and facts? Lets find out" )
    print("+---------------------+")
    print(" PLEASE SELECT AN OPTION ")
    print("                   ")
    print( "1. Play True or False Quiz" )
    print(" 0. Quit" )
    print("+---------------------+")

    choice = input("Enter 1 or 0")
    if choice =="1"
        play_tof_quiz
    elif choice == "0":
        print("Thanks for playing! :) ")
        quit()

main_menu()
