"""
Spotify Coded by my SI Spring '23 Regulars :)
By: Christian Morgado's SI Session Attendees

__str__ functions coded by me to manually test in main :p
"""

class Song:
    __slots__ = ["__name", "__author", "__album", "__duration"]

    def __init__(self, name, author, album, duration):
        self.__name = name    
        self.__author = author
        self.__album = album
        self.__duration = duration

    def getDuration(self):
        return self.__duration

    def __eq__(self, other):
        if type(self) == type(other):   #The type() function returns the TYPE of the object you are using
            return (self.__name == other.__name) and (self.__author == other.__author) and (self.__album == other.__album) and (self.__duration == other.__duration) 
        else:
            return False
        
    def __str__(self):
        return self.__name + " by: " + self.__author
        
class Playlist:
    __slots__ = ["__name", "__songs", "__author", "__duration"]

    def __init__(self, name, author):
        self.__name = name
        self.__author = author
        self.__songs = []
        self.__duration = 0

    def addSong(self, song):
        self.__songs.append(song)
        self.__duration += song.getDuration()

    def removeSong(self, song):
        for index in range(len(self.__songs)):
            if song == self.__songs[index]:
                self.__songs.pop(index)
                break

    def __str__(self):
        string = "["
        for index in range(len(self.__songs)):
            string += str(self.__songs[index])
            if(index != len(self.__songs)-1):
                string += ", "
        return string + "]"


def main():
    song1 = Song("poop", "me", "shits and giggles", 12)
    song2 = Song("fart", "me", "shits and giggles", 32)
    song3 = Song("pee", "me", "shits and giggles", 2)
    song4 = Song("cum", "me", "shits and giggles", 100)

    playlist = Playlist("my favorite shits and giggles", "me2")
    print(playlist)
    playlist.addSong(song1)
    print(playlist)
    playlist.addSong(song2)
    playlist.addSong(song3)
    print(playlist)
    playlist.removeSong(song2)
    print(playlist)
    playlist.removeSong(song2)
    print(playlist)

main()

