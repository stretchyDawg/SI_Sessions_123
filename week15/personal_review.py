import csv
import song
import node_stack
import array_queue
# If your array_queues or node_stacks don't work, feel free to send me a message and I'll send you my implementation :)

"""
BACK TO CSV FILES
Songs are stored in a csv file in this format:
Title,Length,Author,Album
Only If,0:1:40,Apollo XXI,Steve Lacy
...

Create a function that takes a csv file of songs and makes Song objects out of them. Have it return all of those songs in some collection.
For reference, here is the Song class we have made (4 TIMES) this semester in our sessions:
"""
def csv_songs(filename):
    songs = []
    with open(filename) as file:
        csv_reader = csv.reader(file)
        for record in csv_reader:
            print(record)
            title = record[0]
            time = record[1].split(":")
            author = record[3]
            songs.append(song.Song(title, author, song.Time(time[0], time[1], time[2])))
    return songs
  
print("\n", csv_songs("week15/songs.csv"), sep = "")
            

"""
PALINDROME:
Create a is_palindrome() function that takes in a string. Use stacks and queues to return a string representing whether 
the given string is a palindrome or not. Should not be case sensitive (i.e. "Radar" and "radar" should both return True).
"""

def is_palindrome(string):
    string = string.lower()
    
    stack = node_stack.Stack()
    queue = array_queue.Queue()
    
    for char in string:
        stack.push(char)
        queue.enqueue(char)
        
    while not stack.is_empty() or not queue.is_empty():
        # Uncomment these to see the stacks and queues in action
        # print("Stack:", stack)
        # print("Queue:", queue)
        if stack.pop() != queue.dequeue():
            return False
    return True

print(is_palindrome("Radar"))
print(is_palindrome("radar"))
print(is_palindrome("Mya"))