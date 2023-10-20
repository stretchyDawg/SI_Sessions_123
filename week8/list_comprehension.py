def for_comp():
    """
    Make a list comprehension statement AND a for loop that follows this prompt:
    Give me all of the odd values between 1 and 10
    """
    com = [x for x in range(1, 11) if x % 2 == 1]
    print("Comprehension List:", com)
    
    for_ = []
    for x in range(1, 10):
        if x % 2 == 1:
            for_.append(x)
    print("For Loop List:",for_)
    

def activities():
    """
    1: Give me a list of the square root of all odd numbers from 1-20.
    2: Give me 15 zeroes.
    3: Given the string “Bobby”, give me all of the uppercase and lowercase B's. 
    """
    x1 = [x**.5 for x in range(1, 21) if x % 2 == 1]
    print(x1)
    x2 = [0 for _ in range(15)]
    print(x2)
    x3 = [letter for letter in "Bobby" if letter.lower() == "b"]
    print(x3)

def main():
    # v = [letter for letter in "I love SI!"]
    # w = [x for x in range(11)]
    # x = [x+1 for x in range(11)]
    # y = [x for x in range(11) if x % 2 == 0]
    # z = [chr(ord(letter)+1) for letter in "foobar"]
    # lists = [v, w, x, y, z]
    print()
    # for lst in lists:
    #     print(lst)
    activities()
    print()
    for_comp()



main()