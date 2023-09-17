"""
Unit Test file for guessing.py
@ChristianMorgado
"""

import guessing 
import random

def test_check_guess_less_than_1():
    # setup
    expected = "Guess out of range!"
    answer = 4
    guess = 0

    # invoke
    actual = guessing.check_guess(answer, guess)

    # analyze
    assert actual == expected

def test_check_guess_higher_than_10():
    # setup
    expected = "Guess out of range!"
    answer = 4
    guess = 11

    # invoke
    actual = guessing.check_guess(answer, guess)

    # analyze
    assert actual == expected

def test_check_guess_3_less_than_4():
    # setup
    expected = "Too low!"
    answer = 4
    guess = 3

    # invoke
    actual = guessing.check_guess(answer, guess)

    # analyze
    assert actual == expected

def test_check_guess_5_greater_than_4():
    # setup
    expected = "Too high!"
    answer = 4
    guess = 5

    # invoke
    actual = guessing.check_guess(answer, guess)

    # analyze
    assert actual == expected

def test_check_guess_correct_4():
    # setup
    expected = "Correct!"
    answer = 4
    guess = 4

    # invoke
    actual = guessing.check_guess(answer, guess)

    # analyze
    assert actual == expected