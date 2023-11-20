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
        
    def get_time_as_string(time):
        return '{}:{:02}:{:02}'.format(time.__hours, time.__minutes, time.__seconds)


class Song:
    __slots__ = ["__name", "__author", "__duration"]

    def __init__(self, name, author, duration):
        self.__name = name    
        self.__author = author
        self.__duration = duration
        
    def get_duration(self):
        return self.__duration
        
class Playlist:
    __slots__ = ["__title", "__songs", "__user", '__total_duration']
    
    def __init__(self, title, user, songs):
        self.__title = title  
        self.__user = user
        self.__songs = songs
        self.__total_duration = self.calculate_total_duration()
        
    def calculate_total_duration(self):
        total_hrs = 0
        total_min = 0
        total_sec = 0
        for song in self.__songs:
            song_duration = song.get_duration()
            total_hrs += song_duration.get_hours()
            total_min += song_duration.get_minutes()
            total_sec += song_duration.get_seconds()
        return Time(total_hrs, total_min, total_sec)
        
    # Add/Remove songs
    def add_song(self, given_song):
        self.__songs.append(given_song)
        self.__total_duration = self.calculate_total_duration()
        
    def remove_song(self, index):
        self.__songs.pop(index)
        self.__total_duration = self.calculate_total_duration()
    
    def print_playlist(self):
        print(self.__title)
        print(self.__user)
        print(self.__songs)
        print(self.__total_duration.get_time_as_string())
        
def main():
    song_list = [Song("one", "0", Time(0, 0, 1)),
                 Song("two", "0", Time(0, 2, 13)),
                 Song("three", "0", Time(0, 7, 43)),
                 Song("four", "0", Time(1, 20, 11))]
    
    print()
    playlist = Playlist("poop", "peep", song_list)
    playlist.print_playlist()
    print()
    playlist.add_song(Song("five", "0", Time(1,1,1)))
    playlist.print_playlist()
    print()
    playlist.remove_song(4)
    playlist.print_playlist()
    
main()