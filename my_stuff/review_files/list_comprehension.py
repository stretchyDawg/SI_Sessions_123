def main():
    """
    expression for item in sequence
    """
    
    x = [n for n in range(1, 11)]
    print(x)

    """
    All of the letters in the string "foobar"
    15 0s
    The integers 0-12
    The even integers between 0 and 20
    The integers less than 50 divisible by 3 or 5
    """
    x1 = [letter for letter in "foobar"]
    print(x1)
    x1 = [chr(ord(letter)+1) for letter in "foobar"]
    print(x1)
    x2 = [0 for _ in range(15)]
    print(x2)
    x3 = [x for x in range(13)]
    print(x3)
    x4 = [x for x in range(21) if x % 2 == 0]
    print(x4)
    x5 = [x for x in range(51) if x % 3 == 0 or x % 5 == 0]
    print(x5)

main()



