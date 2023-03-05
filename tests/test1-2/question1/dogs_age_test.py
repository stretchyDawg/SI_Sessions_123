"""
This is the second part of question 1.

Write as many tests for the "dog_age" module as you think are necessary to fully 
test the functions therein. If any of your tests fail, use the feedback from 
Pytest to fix your code!

Your tests will be expected to exemplify the qualities of a good test.
"""

import dogs_age

def test_human_years_neg_100():
    #setup
    dog_years = -100
    expected = None

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

def test_human_years_less_than_or_equal_to_zero():
    #setup
    dog_years = 0
    expected = None

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

def test_human_years_one():
    #setup
    dog_years = 1
    expected = 15

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

def test_human_years_two():
    #setup
    dog_years = 2
    expected = 15 + 9

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

def test_human_years_three():
    #setup
    dog_years = 3
    expected = 15 + 9 + (5 * (dog_years-2))

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

def test_human_years_ten():
    #setup
    dog_years = 10
    expected = 15 + 9 + (5 * (dog_years-2))

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

def test_human_years_hundred():
    #setup
    dog_years = 100
    expected = 15 + 9 + (5 * (dog_years-2))

    #invoke
    actual = dogs_age.human_years(dog_years)

    #analyze
    assert expected == actual

