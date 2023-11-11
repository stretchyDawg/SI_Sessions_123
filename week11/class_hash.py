class Song:
    __slots__ = ['name', 'author', 'length']

    def __init__(self, name, author, length):
        self.name = name # string
        self.author = author # string
        self.length = length # int

def hash_song(song):
    """
    Fast: Yes (O(n) based on the name and author of the given song, which are short)
    Consistent: Yes
    Minimal Collisions: Yes, hash code is based on the name and length of the song, along with advanced calculations that will provide vastly different answers if two given songs have similar lengths and titles.
    """
    hash_code = 0
    for char_index in range(len(song.name)):
        hash_code += ((ord(song.name[char_index]) * (31**(len(song.name)-(char_index-1)))) / song.length) 
        for char_index in range(len(song.author)):
            hash_code += ((ord(song.author[char_index]) * (29**(len(song.author)-(char_index-1)))) / song.length) 
    
    return hash_code

def main():
    song = Song("fart", "farter", 10)
    print(song.name, song.author, song.length)
    song2 = Song("fard", "farter", 10)
    song3 = Song("fart", "farted", 10)
    song4 = Song("fart", "farter", 9)
    song5= Song("farte", "fartere", 10)
    print(hash_song(song))
    print(hash_song(song2))
    print(hash_song(song3))
    print(hash_song(song4))
    print(hash_song(song5))
    # All of these hash functions provide different hash codes for similar data (although, yes the hash codes are similar) 

main()