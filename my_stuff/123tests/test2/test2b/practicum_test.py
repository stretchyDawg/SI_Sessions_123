"""
Python unit test provided to students to test their comics.py implementation.

Rather than trying to run all of the tests at once, uncomment them one at a 
time to verify that your code is working as expected.

Remember, you can select a block of code and type CTRL+/ (or Command+/) to 
comment/uncomment it.
"""

from practicum import * # this will not work until you create the module
import arrays

"""
Tests for count_letters.
"""

def test_count_letters_empty():
    # setup
    letters = ""
    string = ""
    expected = 0

    # invoke
    actual = count_letters(letters, string)

    # analyze
    assert expected == actual

def test_count_letters_0():
    # setup
    letters = "x"
    string = "zebra"
    expected = 0

    # invoke
    actual = count_letters(letters, string)

    # analyze
    assert expected == actual

def test_count_letters_5():
    # setup
    letters = "aeiou"
    string = "Abraham Lincoln"
    expected = 5

    # invoke
    actual = count_letters(letters, string)

    # analyze
    assert expected == actual

"""
Tests for count_comics.
"""

def test_count_comics_ludo_bagman():
    """
    Test that expects 0 to be returned for a creator that does not appear in
    the provided database.
    """
    # setup
    filename = "data/comics.csv"
    creator = "Ludo Bagman"
    expected = 0

    # invoke
    actual = count_comics(filename, creator)

    # analyze
    assert expected == actual

def test_count_comics_stan_lee():
    # setup
    filename = "data/comics.csv"
    creator = "Stan Lee"
    expected = 10

    # invoke
    actual = count_comics(filename, creator)

    # analyze
    assert expected == actual

def test_count_comics_brian_michael_bendis():
    # setup
    filename = "data/comics.csv"
    creator = "Brian Michael Bendis"
    expected = 616

    # invoke
    actual = count_comics(filename, creator)

    # analyze
    assert expected == actual

def test_count_comics_todd_mcfarlane():
    # setup
    filename = "data/comics.csv"
    creator = "Todd McFarlane"
    expected = 118

    # invoke
    actual = count_comics(filename, creator)

    # analyze
    assert expected == actual

"""
Tests for array_sum.
"""

def test_array_sum_start_greater():
    # setup
    an_array = arrays.Array(0)
    start = 0
    end = len(an_array) - 1
    expected = 0

    # invoke
    actual = array_sum(an_array, start, end)

    # analyze
    assert expected == actual


def test_array_sum_one():
    # setup
    an_array = arrays.Array(1)
    start = 0
    end = len(an_array) - 1
    an_array[0] = 5
    expected = 5

    # invoke
    actual = array_sum(an_array, start, end)

    # analyze
    assert expected == actual

def test_array_sum_odd():
    # setup
    an_array = arrays.Array(5)
    start = 0
    end = len(an_array) - 1
    an_array[0] = 5
    an_array[1] = 4
    an_array[2] = 3
    an_array[3] = 6
    an_array[4] = 7
    expected = 25

    # invoke
    actual = array_sum(an_array, start, end)

    # analyze
    assert expected == actual

def test_array_sum_even():
    # setup
    an_array = arrays.Array(6)
    start = 0
    end = len(an_array) - 1
    an_array[0] = 1
    an_array[1] = 2
    an_array[2] = 3
    an_array[3] = 5
    an_array[4] = 7
    an_array[5] = 11
    expected = 29

    # invoke
    actual = array_sum(an_array, start, end)

    # analyze
    assert expected == actual