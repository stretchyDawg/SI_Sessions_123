"""
Pracitcum Test Review 2 for my SI Session
@ChristianMorgado
"""

def iterating_through_string():
    name = "Christian Morgado"
    for char in name:
        print(char)

def iterating_through_string():
    name = "aaron earned an iron urn"
    split_name = name.split("r")
    # Tokens: ["aa", "on ea", "ned an i", "on u", "n"]
    for token in split_name:
        print(token)

def for_loop():
    for _ in range(10):
        print("hello :)")

def for_loop_seq():
    sequence = "hello :)"
    for char in sequence:
        print(char)

def while_loop():
    x = 0
    while x < 5:
        print("hello :)")
        x += 1

def main():
    iterating_through_string()

if __name__ == "__main__":
    main()


