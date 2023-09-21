"""
GRADING ACTIVITY (part 1):
Create a function that takes in a grade from 0-100. Return a letter based on the grade given:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Then, create a main function and ask the user to input their grade, and print their grade in this format:
“Your score is <inputted_score>. Your grade is <letter_grade>.”
"""
def grade(score):
    grade = "invalid"
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    elif score < 60:
        grade = "F"
    return "Your score is " + str(score) + ". Your grade is " + str(grade) + "."

def main():
    score = int(input("Please input your score: "))
    print(grade(score))

if __name__ == "__main__":
    main()

"""
GRADING ACTIVITY (part 3):
Write an example of a runtime and semantic error that can occur with this function (since we coded the function, we know syntax errors won’t occur, as discussed before in this SI Session). We’ll discuss how we can avoid these after we list them:

1- Runtime (ValueError): User inputs a string that can’t be casted into an int in the input statement.
2- Semantic: User inputs a number not in the range of 0-100. 
"""