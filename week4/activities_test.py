import activities

def test_is_even_true():
    # setup
    expected = True

    # invoke
    actual = activities.is_even(0)

    # analyze
    assert actual == expected

def test_is_even_false():
    # setup
    expected = False

    # invoke
    actual = activities.is_even(1)

    # analyze
    assert actual == expected