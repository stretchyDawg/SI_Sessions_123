def using_sets():
    """
    USING SETS:
    Setup: Make two spaces on the whiteboard, one space for your code (which will follow Python syntax) and another space for your code output. Write your output like this: (this is example output, don’t write the fruits)
    >> apple
    >> banana
    >> pineapple

    1: Declare a main function to do some work with sets.
    2: Declare an empty set.
    3: Print the empty set.
    4: Add some values of multiple data types into that set.
    5: Print that set.
    6: Declare a new set with your favorite albums as strings already inside.
    7: Print the length of the album set.
    8: Remove the first item in your set.
    9: Print the album set after removing the first value.
    10: Create another new set out of your (or someone in your groups) name.
    Hint: it's similar to how you made an empty set
    11: Iterate through the set of your name and print each letter.
    12: Check if the letter 'e' is in that name, and if it is, print whatever you want (if you can't think of something just print “fart”)
    """
    empty_set = set()
    print(empty_set)
    empty_set.add(1)
    empty_set.add(2)
    print(empty_set)
    
    album_set = {"Apollo XXI", "Atlanta Millionaires Club", "Ego Death", "Isolation"}
    print("Length of album set:", len(album_set))
    album_set.remove("Apollo XXI")
    print(album_set)
    
    name_set = set("Christian")
    for value in name_set:
        print(value, end = " ")
    if 'e' in name_set:
        print("\nfart")
    elif 'C' in name_set:
        print("\npoop")
    
def using_dicts():
    """
    USING DICTIONARIES:
    Setup: On the whiteboard you can either erase your set setup, you can keep your main function declaration (if you do make sure to take pictures) or make a separate space for some more code. Write your output the same way as before.

    1: Declare an empty dictionary. (Fun fact, there are two ways to do this).
    2: Print the empty dictionary.
    3: Print the length of the empty dictionary.
    4: Declare a new dictionary with 3 key:value pairs already inside of it. Have the value be some of your favorite movies (by putting the title as a string) and the key being the length of the title string. An example:
    key = 7
    value = Bottoms
    5: Print the movie dictionary.
    6: Iterate through the movie dictionary and print each value.
    7: Check if there is a movie with the length of 5 letters in it. If there is one, print it. 
    8: Now, make a new empty dictionary, use a different method then you used in number 1.
    9: Add some key:value pairs to the new dictionary. The values will be the names of the people in your group, the keys will be the length of the names (same as before).
    10: Print the new name dictionary. 
    """
    empty1 = {}
    print(empty1)
    print(len(empty1))
    
    movie_dict = {9 : "Superbad", 14 : "Apocalypse Now", 13 : "Scott Pilgrim"}
    print(movie_dict)
    for key in movie_dict:    # variable name doesn't matter, it'll iterate through the keys no matter what
        print(key)
    if 5 in movie_dict:
        print('fart')
    elif 13 in movie_dict:
        print('poop')
        
    empty2 = dict()
    empty2[9] = "Christian"
    print(empty2)
        
    

def main():
    print("\n-- Using Sets --")
    using_sets()
    print("\n -- Using Dictionaries --")
    using_dicts()

if __name__ == "__main__":
    main()