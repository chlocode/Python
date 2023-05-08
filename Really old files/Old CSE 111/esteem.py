def main():
    
  print("This program is an implementation of the Rosenberg")
  print("Self-Esteem Scale. This program will show you ten")
  print("statements that you could possibly apply to yourself.")
  print("Please rate how much you agree with each of the")
  print("statements by responding with one of these four letters:")

  print("D means you strongly disagree with the statement.")
  print("d means you disagree with the statement.")
  print("a means you agree with the statement.")
  print("A means you strongly agree with the statement.")


  #question1
  print("1. I feel that I am a person of worth, at least on an equal plane with others.")
  answer1=input("Enter D, d, a, or A:")
  score1=positive_statement_grade(answer1)
  print(score1)

  #question2
  print("2. I feel that I have a number of good qualities.")
  answer2=input("Enter D, d, a, or A:")
  score2=positive_statement_grade(answer2)
  print(score2)

  #question3
  print("3. All in all, I am inclined to feel that I am a failure.")
  answer3=input("Enter D, d, a, or A:")
  score3=negative_statement_grade(answer3)
  print(score3)

  #question4
  print("4. I am able to do things as well as most other people.")
  answer4=input("Enter D, d, a, or A:")
  score4=positive_statement_grade(answer4)
  print(score4)

  #question5
  print("5. I feel I do not have much to be proud of.")
  answer5=input("Enter D, d, a, or A:")
  score5=negative_statement_grade(answer5)
  print(score5)

  #question6
  print("6. I take a positive attitude toward myself.")
  answer6=input("Enter D, d, a, or A:")
  score6=positive_statement_grade(answer6)
  print(score6)

  #question7
  print("7. On the whole, I am satisfied with myself.")
  answer7=input("Enter D, d, a, or A:")
  score7=positive_statement_grade(answer7)
  print(score7)

  #question8
  print("8. I wish I could have more respect for myself.")
  answer8=input("Enter D, d, a, or A:")
  score8=negative_statement_grade(answer8)
  print(score8)

  #question9
  print("9. I certainly feel useless at times.")
  answer9=input("Enter D, d, a, or A:")
  score9=negative_statement_grade(answer9)
  print(score9)

  #question10
  print("10. At times I think I am no good at all.")
  answer10=input("Enter D, d, a, or A:")
  score10=negative_statement_grade(answer10)
  print(score10)

  #print total
  total=calc_score(score1,score2,score3,score4,score5,score6,score7,score8,score9,score10)
  print(f"Your score is: {total}")

def calc_score(ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10):
    total= ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8+ans9+ans10
    return total

def negative_statement_grade(answer):
    if answer=="D":
        score=3
    elif answer=="d":
        score=2
    elif answer=="a":
        score=1
    elif answer=="A":
        score=0
    return score

def positive_statement_grade(answer):
    if answer=="D":
        score=0
    elif answer=="d":
        score=1
    elif answer=="a":
        score=2
    elif answer=="A":
        score=3
    return score

main()

