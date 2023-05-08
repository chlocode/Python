def main():
    print("The Rosenberg self-esteem scale is a self-esteem measure developed by the sociologist Morris Rosenberg in 1965. It is still used in social-science research today. To complete the measure, a person completes a survey that contains the following ten statements.")

    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans1=input("Enter a, b, c, or d:")
    score1=positive_score(ans1)
    print(score1)
    
    print("2. I feel that I have a number of good qualities.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans2=input("Enter a, b, c, or d:")
    score2=positive_score(ans2)

    print("3. All in all, I am inclined to feel that I am a failure.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans3=input("Enter a, b, c, or d:")
    score3=negative_score(ans3)

    print("4. I am able to do things as well as most other people.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans4=input("Enter a, b, c, or d:")
    score4=positive_score(ans4)

    print("5. I feel I do not have much to be proud of.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans5=input("Enter a, b, c, or d:")
    score5=negative_score(ans5)

    print("6. I take a positive attitude toward myself.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans6=input("Enter a, b, c, or d:")
    score6=positive_score(ans6)

    print("7. On the whole, I am satisfied with myself.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans7=input("Enter a, b, c, or d:")
    score7=positive_score(ans7)

    print("8. I wish I could have more respect for myself.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans8=input("Enter a, b, c, or d:")
    score8=negative_score(ans8)

    print("9. I certainly feel useless at times.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans9=input("Enter a, b, c, or d:")
    score9=negative_score(ans9)

    print("10. At times I think I am no good at all.")
    print("a. Strongly Disagree\nb. Disagree\nc. Agree\nd. Strongly Agree")
    ans10=input("Enter a, b, c, or d:")
    score10=negative_score(ans10)

   
    score=total_score(score1, score2, score3, score4, score5, score6, score7, score8, score9, score10)
    print(f"your score is:{score}")
    
def positive_score(ans):
    if ans=="a":
        score=0
    elif ans=="b":
        score=1
    elif ans=="c":
        score=2
    else:
        score=3
    return score

def negative_score(ans):
    if ans=="a":
        score=3
    elif ans=="b":
        score=2
    elif ans=="c":
        score=1
    else:
        score=0
    return score

def total_score(score1, score2, score3, score4, score5, score6, score7, score8, score9, score10):
    total=score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    return total
if __name__ == "__main__":
    main()