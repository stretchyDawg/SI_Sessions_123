from practicum import *
import arrays
import array_utils

"""
As you solve each problem, uncomment the corresponding tests so that you can
verify that your solution works.

Hint: Select the test and press CTRL-/ (or Command-/ on Mac) to toggle the 
comment block.
"""

def test_sum_of_digits_1234():
    # setup
    number = 1234
    expected = 10

    # invoke
    actual = sum_of_digits(number)

    # analyze
    assert expected == actual

def test_sum_of_digits_float():
    # setup
    number = 3.14159
    expected = 23

    # invoke
    actual = sum_of_digits(number)

    # analyze
    assert expected == actual

def test_sum_of_digits_negative():
    # setup
    number = -27.5
    expected = 14

    # invoke
    actual = sum_of_digits(number)

    # analyze
    assert expected == actual

def test_odd_array_copy_empty():
    # setup
    an_array = arrays.Array(0)
    
    # invoke
    actual = odd_array_copy(an_array)

    # analyze
    assert 0 == len(actual)

def test_odd_array_copy_one_odd():
    # setup
    an_array = arrays.Array(1, 3)
    
    # invoke
    actual = odd_array_copy(an_array)

    # analyze
    assert 1 == len(actual)
    assert 3 == actual[0]

def test_odd_copy_one_even():
    # setup
    an_array = arrays.Array(1, 6)
    
    # invoke
    actual = odd_array_copy(an_array)

    # analyze
    assert 0 == len(actual)

def test_odd_copy_one_range():
    # setup
    an_array = array_utils.range_array(5, -1, -1)
    
    # invoke
    actual = odd_array_copy(an_array)

    # analyze
    assert 3 == len(actual)
    assert 5 == actual[0]
    assert 3 == actual[1]
    assert 1 == actual[2]

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

def test_cast_to_int_empty():
    # setup
    a_string = ""
    expected = 0

    # invoke
    actual = cast_to_int(a_string)

    # analyze
    assert expected == actual

def test_cast_to_int_one():
    # setup
    a_string = "5"
    expected = 5

    # invoke
    actual = cast_to_int(a_string)

    # analyze
    assert expected == actual

def test_cast_to_int_1234():
    # setup
    a_string = "1234"
    expected = 1234

    # invoke
    actual = cast_to_int(a_string)

    # analyze
    assert expected == actual
