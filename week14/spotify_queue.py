import song
import array_queue

class SpotifyQueue:
    __slots__ = ["__current", "__queue", "__history"]
    
    def __init__(self):
        self.__current = None
        self.__queue = array_queue.Queue()
        self.__history = []
        
    def add_song(self, song):
        pass
    
    
    def __str__(self):
        return str(self.__queue)
        

def main():
    queue = SpotifyQueue()
    queue.add_song(song.Song("Cannonball", "The Breeders", song.Time(0, 2, 2)))
    print(queue)

if __name__ == "__main__":
    main()