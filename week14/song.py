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



class Song:
    __slots__ = ["__name", "__author", "__duration"]

    def __init__(self, name, author, duration):
        self.__name = name    
        self.__author = author
        self.__duration = duration
        
    def get_duration(self):
        return self.__duration
    
    def __str__(self):
        return str(self.__name) + " by " + str(self.__author) + ": " + str(self.__duration)
    
def main():
    time_a = Time(0, 2, 21)
    print(time_a)
    song_a = Song("Guide", "Steve Lacy", time_a)
    print(song_a)
    
if __name__ == "__main__":
    main()