"""
SPOTIFY (pt1):
@ChristianMorgado -- Fall 2023

For this session we will be coding Spotify in Python! For all of these questions you can use the Spotify app as a reference for how things should be done (if your confused on what the program should look like, turn to the Spotify app).

If the instructions don't specify which parameters or data structures to use, that means it is up to you to choose. 
-	1: Create an implementation of a song entry represented by some data structure. To do this you will make a create_song() function. We will discuss the parameters!
-	2: Create an implementation of a playlist, which is some collection of songs. When you first create a playlist, you must insert 3 songs. To do this you will make a create_playlist() function.
-	3.1: For the playlist, create an add_song(playlist, song) function that adds a given song to a given playlist.
-	3.2: For the playlist, create a remove_song(playlist) function that removes a song from a given playlist.
-	4: For the playlist, make a get_runtime(playlist) function that returns the total runtime of a given playlist.
-	5: For the playlist, create a search(playlist, name) function that searches for a song, given its name, in a given playlist. Return a Boolean representing if its found or not.
-	6: Create an implementation for a user represented by some data structure. A users properties consists of a name and a collection of playlists. To do this you will make a create_user(name, playlists) function.
    -   Something to think about... when you make a Spotify account, what playlist does EVERY user have?
-	7.1: For the user, create an add_playlist(user, playlist) function that adds a given playlist to a given users collection of playlists.
-	7.2: For the user, create a remove_playlist(user) function that removes a playlist in a given users collection of playlists.
-	8: For the user, create an artist_count(user, given_artist) function that finds the amount of songs by a given artist in a given users collection of playlists.  
-	9: For the playlist, make a shuffle(playlist) function that shuffles the order of the songs of a given playlist. 
    -   (YOU MAY SKIP THIS IF TIME IS RUNNING OUT)
-	10: Create a print_user(user) function that prints a users name and playlists in this format:
        Name: <name>
        Playlist 1: <playlist_contents>
        Playlist 2: …
        …     
        
(pt2 will involve python class syntax)   
"""