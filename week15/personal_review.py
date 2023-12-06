import csv
import song

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
LETS FINALLY MAKE AN ALBUM
Create an Album class that takes in 3 parameters in its constructor, a Name, an Author, and a filename.
The Album class should have these properties:
- Name
- Author
- Songs
- Total Runtime

Using the same csv file as before, go through the file and take every song that matches the author and album name, 
SERIALIZE it to a Song class, and add it to the collection of songs in the album.
"""

"""
Maybe make a dictionary that ties each album to its songs???????
"""

