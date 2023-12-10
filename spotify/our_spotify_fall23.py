"""
Prompt:
<input your code below>

SPOTIFY
0: I have provided you a Time class. Please use it for any duration fields. I have also 
provided 3 .csv files for you to use for personal testing :) if you want you could make 
unit tests to test your own code. 


1: A Song has a title, author, and a duration. Create a class representing a song, that 
class should contain a constructor function, getters for each field, and a __str__ function 
in this format:
"'<song_title>' by '<song_author>': <song_duration>"

A song is greater than another song if the title is alphabetically greater than another song.
(i.e. the song Amandla's Interlude by Steve Lacy is 'greater than' N Side by Steve Lacy because it comes first in the alphabet)

Songs should also be able to be put in sets! (If you don't know what this means feel free to ask me).

Create a few Songs in the main() function below and make a set of 3 songs. Additionally, make
a list of songs and use the sort() function on them.



2: A Playlist has a title, author, and some collection of songs. Create a class to represent this
like you did before. What data types will you use for each field? That is up to you. Think about
how playlists work in spotify, users make them and they can add and remove songs at will.

Functionality:
    - Create an add_song() and remove_song() method for the Playlist class that adds and removes songs to
      the collection of songs. 
    - You should be able to use the len() function on a playlist so that it can return the amount of songs
      inside the collection of songs. 
    - A playlist is greater than another playlist if it has more songs.
    - Create a __str__ function that displays the title, author, and songs in a readable format.
    - (Hardest one) Create a get_total_duration() function that calculates the total duration of 
      the whole playlist.

Create a Playlist in the main() function. When you make it, the collection should be empty first, then
you should be able to add songs to it. 



3: An Album has a title, author, and some collection of songs. Create a class to represent this
like you did before. It is very similar to the playlist class, except artists are the ones who
make albums, and typically they aren't able to add or remove songs to an album. Based on this,
which data structures should we use?

When using the Album class in the main() function, you can pass in the collection of songs instead of
making an empty one first, since you won't be changing the songs.

Functionality:
    - You should be able to use the len() function on a playlist so that it can return the amount of songs
      inside the collection of songs. 
    - Create a __str__ function that displays the title, author, and songs in a readable format.

Create an Album in the main() function :)


4: A SpotifyQueue has two fields, the current song being listened to and the actual queue of songs. Create
a class to represent this just like you did before.

SpotifyQueue functionality:
    -  Should be able to add songs to the queue
    -  Should be able to play songs
    -  Should be able to skip songs
    -  Should have a __str__ function that portrays the queue in a readable format
        - Hint: It's easier than you think, the node_queue implementation basically does this for you
    -  Should be able to add playlists/albums to the queue
        - (you pass in an album or playlist and it adds every song to that on the queue)
    - Should be able to clear the queue
        - Essentially emptying the queue
    -  Should be able to go back to old songs
        - (this is REALLY hard, like way harder than anything they'd ask you on the test, if you want you 
           could try to answer it by commenting what you would do) 
           
"""
class Time:
    __slots__ = ['__hours', '__minutes', '__seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
       
    # Getters 
    def get_hours(self):
        return self.__hours
    def get_minutes(self):
        return self.__minutes
    def get_seconds(self):
        return self.__seconds
        
    # Special Methods
    def __str__(self):
        return '{}:{:02}:{:02}'.format(self.__hours, self.__minutes, self.__seconds)

def main():
    pass

if __name__ == "__main__":
    main()