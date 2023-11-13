"""
Implement your solution to the practicum in this file.

"""
PHONETIC_ALPHABET = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", 
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", 
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]

import re

# Question 1
def euclidean_distance(seq1, seq2):
    """
    Returns an euclidean distance given 2 sequences.
    """
    if len(seq1) != len(seq2):
        return None
    else:
        sum = 0
        for index in range(len(seq1)):    
            value1 = seq1[index]
            value2 = seq2[index]
            sum = sum + ((value1 - value2)**2)
        euclidean_distance = (sum)**0.5
        return euclidean_distance

# Question 2
def is_pangram(str):
    """
    Returns a boolean value.
    True if the given string is a pangram.
    False if the given string is not.
    """
    str = str.lower()
    str_letters = re.findall("[a-zA-Z]", str)
    pangram_set = set()
    for letter in str_letters:
        pangram_set.add(letter)
    if len(pangram_set) == 26:
        return True
    else:
        return False

# Question 3 
def phonetic_translation(str):
    """
    Returns a phonetic translation of a string (as a list of words).
    """
    str = str.lower()
    str_letters = re.findall("[a-zA-Z]", str)
    phonetic_str = []
    for letter in str_letters:
        for phonetic_letter in PHONETIC_ALPHABET:
            if letter == phonetic_letter[0].lower():
                phonetic_str.append(phonetic_letter)
    return phonetic_str

# Question 4
def words_by_letter(str):
    """
    Returns a dictionary that ties each unique word as a value to the letter that starts them as a key.
    """
    letter_dict = dict()
    if len(str) == 0:
        return letter_dict
    split_string = str.split(" ")
    for word in split_string:
        if word[0] in letter_dict:
            letter_dict[word[0]].add(word)
        else:
            letter_dict[word[0]] = set()
            letter_dict[word[0]].add(word)
    return letter_dict

def main():
    # a_string = "The cat in the hat is back with a bright blue bat out in " \
    #     "the back"
    # answer_dict = words_by_letter(a_string)
    
    # sorted_keys = sorted(answer_dict.keys())
    # for key in sorted_keys:
    #     print(key, ":", answer_dict[key])

    a_string = "SI stands for Supplemental Instruction"
    print(words_by_letter(a_string))
    


if __name__ == "__main__":
    main()