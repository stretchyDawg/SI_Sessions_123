import grading

"""
GRADING ACTIVITY (part 2):
Create one test function for this function.
"""

def test_grade_pass():
    #setup
    score = 69
    grade = "D"
    expected = "Your score is " + str(score) + ". Your grade is " + str(grade) + "."

    #invoke
    actual = grading.grade(score)

    #analyze
    assert actual == expected
