import song
import array_queue

class SpotifyQueue:
    __slots__ = ["__current", "__queue"]
    
    def __init__(self):
        self.__current = None
        self.__queue = array_queue.Queue()
        
    def add_song(self, song):
        self.__queue.enqueue(song)
        
    def add_playlist(self, playlist):
        for song in playlist.getSongs():
            self.__queue.enqueue(song)
        
    def play_song(self):
        self.__current = self.__queue.front()
        self.__queue.dequeue()
    
    def __str__(self):
        return "Current Song: " + str(self.__current) + "\nQueue: " + str(self.__queue)
        

def main():
    queue = SpotifyQueue()
    queue.add_song(song.Song("Cannonball", "The Breeders", song.Time(0, 2, 2)))
    queue.add_song(song.Song("Cool Schmool", "Bratmobile", song.Time(0, 2, 2)))
    queue.add_song(song.Song("Come Out and Play", "The Offspring", song.Time(0, 3, 18)))

    print()
    print(queue)
    queue.play_song()
    print(queue)
    queue.play_song()
    print(queue)
    print()
    
    playlist = song.Playlist("Punk Mix", "Christian")
    playlist.addSong(song.Song("akimahenka", "Otoboke Beaver", song.Time(0, 1, 7)))
    playlist.addSong(song.Song("Intro", "Bad Brains", song.Time(0, 0, 23)))
    playlist.addSong(song.Song("Muzzle", "Destroy Boys", song.Time(0, 3, 3)))
    playlist.addSong(song.Song("Teen Mom", "Slutever", song.Time(0, 1, 43)))
    playlist.addSong(song.Song("Banned in D.C.", "Bad Brains", song.Time(0, 5, 5)))
    playlist.addSong(song.Song("Assholes", "Mommy Long Legs", song.Time(0, 3, 23)))
    playlist.addSong(song.Song("Cops / Dogs", "Destructo Disk", song.Time(0, 2, 6)))
    print(playlist)
    
    queue.add_playlist(playlist) 
    print(queue)

if __name__ == "__main__":
    main()