"""
Spotify Assignment REMASTERED
@ChristianMorgado Spring Semester 23

PROMPTS (what I will send them in the discord):
Using your knowledge of lists and tuples, you will be programming Spotify in Python!
Heres what you have to do:
-	1: Create an implementation of a song entry represented by a data structure. To do this you will make a create_song() function. We will discuss the parameters!
-	2: Create an implementation of a playlist, which is a collection of songs. When you first create a playlist, you must insert 3 songs. To do this you will make a create_playlist() function.
-	3.1: For the playlist, create an add_song(playlist, song) function that adds a given song to a given playlist.
-	3.2: For the playlist, create a remove_song(playlist, index) function that removes a song at a given index from a given playlist.
-	4: For the playlist, make a get_runtime(playlist) function that returns the total runtime of a given playlist.
-	5: For the playlist, create a search(playlist, name) function that searches for a song, given its name, in a given playlist. Return a Boolean representing if its found or not.
-	6: Create an implementation for a user represented by a data structure. A users properties consists of a name and a collection of playlists. To do this you will make a create_user(name, playlists) function.
-	7.1: For the user, create an add_playlist(user, playlist) function that adds a given playlist to a given users collection of playlists.
-	7.2: For the user, create a remove_playlist(user, index) function that removes a playlist at a given index in a given users collection of playlists.
-	8: For the user, create an artist_count(user, given_artist) function that finds the amount of songs by a given artist in a given users collection of playlists.  
-	9: For the playlist, make a shuffle(playlist) function that shuffles the order of the songs of a given playlist. (MAY SKIP)
-	10: Create a print_user(user) function that prints a users name and playlists in this format:
        Name: <name>
        Playlist 1:
        Playlist 2:
        …
"""

import random


def make_song(name, artist, runtime):
    """
    1: Create an implementation of a song entry, represented by a data structure. 
    To do this you will make a create_song() function. We will discuss the parameters!
    """
    return (name, artist, runtime)

def make_playlist(song1, song2, song3):
    """
    2: Create an implementation of a playlist, which is a collection of songs. 
    When you first create a playlist, you must insert 3 songs. To do this you 
    will make a create_playlist() function.
    """
    return [song1, song2, song3]

def add_song(playlist, song):
    """
    3.1: For the playlist, create an add_song(playlist, song) that adds a given song to a given playlist.
    """
    playlist.append(song)

def remove_song(playlist, index):
    """
    3.2: For the playlist, create a remove_song(playlist, index) that removes a song at a given index from a given playlist.
    """
    try:
        playlist.pop(index)
    except:
        print("ERROR: Invalid index!")

def get_runtime(playlist):
    """
    4: For the playlist, make a get_runtime(playlist) that returns the total runtime of a given playlist.
    """
    runtime = 0.0
    for song in playlist:
        song_time = song[2]
        runtime += song_time
    return runtime

def search(playlist, given_name):
    """
    5: For the playlist, create a search(playlist, name) function that searches for a song, given its name, 
    in a given playlist. Return a Boolean representing if its found or not.
    """
    for song in playlist:
        song_name = song[0]
        if given_name == song_name:
            return True
    return False

def make_user(name):
    """
    6: Create an implementation for a user represented by a data structure. A users properties consists of 
    a name and a collection of playlists. To do this you will make a create_user(name, playlists) function.
    """
    return (name, [])

def add_playlist(user, playlist):
    """
    7.1: For the user, create an add_playlist(user, playlist) function that adds a given playlist to a given 
    users collection of playlists.
    """
    user[1].append(playlist)

def remove_playlist(user, index):
    """
    7.2: For the user, create a remove_playlist(user, playlist) function that removes a playlist at a given index from a 
    given users collection of playlists.
    """
    try:
        user[1].pop(index)
    except:
        print("ERROR: Invalid index!")

def artist_count(user, given_artist):
    """
    8: For the user, create an artist_count(user, given_artist) function that returns the amount of songs that are by 
    a given artist in a given user's collection of playlists
    """
    playlists = user[1]
    song_count = 0

    if len(playlists) == 0:
        return song_count
    else:
        for playlist in playlists:
            for song in playlist:
                artist = song[1]
                if artist == given_artist:
                    song_count += 1
        return song_count

def shuffle(playlist):
    """
    9: For the playlist, make a shuffle(playlist) function that shuffles the order of the songs of a given playlist.
    """
    length = len(playlist)
    for index in range(length-1, 0, -1):
        random_index = random.randint(0, index)
        temp = playlist[random_index]
        playlist[random_index] = playlist[index]
        playlist[index] = temp
    
    return playlist

def print_user(user):
    """
    10: Create a print_user(user) function that prints a users name and playlists in this format:
    """
    print("Name:", user[0])

    if len(user[1]) != 0:
        for playlist in user[1]:
            print(playlist, sep = "", end = "\n")

def main():
    song1 = make_song("abe", "bee", 10)
    song2 = make_song("ceed", "leed", 20)
    song3 = make_song("creed", "greed", 30)
    playlist1 = make_playlist(song1, song2, song3)
    print(playlist1, "   ", get_runtime(playlist1))
    remove_song(playlist1, 1)
    print(playlist1, "   ", get_runtime(playlist1))
    print(search(playlist1, "creed"))
    print(search(playlist1, "ceed"))
    print("\n")

    print(playlist1)
    add_song(playlist1, ("boo", "a", 119.1))
    add_song(playlist1, ("baa", "a", 1234.32))
    add_song(playlist1, ("bow", "a", 5.2))
    add_song(playlist1, ("aaa", "b", 1))
    add_song(playlist1, ("bbb", "b", 3.98))
    print(playlist1)
    shuffle(playlist1)
    print(playlist1)
    print(get_runtime(playlist1))
    
    print() # Empty user
    christian = make_user("christian")
    print_user(christian)

    print() # One playlist
    add_playlist(christian, playlist1)
    print_user(christian)
    print("Artist count of a:", artist_count(christian, "a"))
    print("Artist count of b:", artist_count(christian, "b"))

    print() # Two playlists
    playlist2 = make_playlist(("123", "a", 12), ("456", "a", 443), ("789", "a", 5000.001))
    add_song(playlist2, ("ccc", "b", .99))
    shuffle(playlist2)
    add_playlist(christian, playlist2)
    print_user(christian)
    print("Artist count of a:", artist_count(christian, "a"))
    print("Artist count of b:", artist_count(christian, "b"))

main()

    