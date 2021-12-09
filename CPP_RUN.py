def get_tof_questions():
#
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

# Show tof statements using a loop
for q in tof_questions:

  # Present statement
  print("True or false: " + s[0] )
  # user enter guess
  guess= input("Enter T or F:")
  # check if guess iis correct
  if guess == s[1]:
      print("Correct!")
    # update score
    score=score + 1
else:
    print("Incorrect :( ")
# Show final score
play_tof_quiz()
