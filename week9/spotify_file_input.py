"""
STORING ALBUMS USING DATA STRUCTURES:
You are given this CSV file of an album (note that the second line is the title of the album and the full length of the album):
Title,Length
Apollo XXI by Steve Lacy, 43:00
Only If,1:40
Like Me,9:04
Playground,3:33
Basement Jack,1:49
Guide,2:21
Lay Me Down,3:03
Hate CD,2:40
In Lust We Trust,2:00
Love 2 Fast,3:42
Amandla's Interlude,3:10
N Side,3:42
Outro Freestyle/4ever,6:14

Create a function that, given a file name of any CSV file representing an album, returns a tuple in this form:
(<title>, <total_length>, <list_of_all_songs>)
"""
import csv

def album_file(filename):
    title = input("Please enter a title of an album:")
    author = input("Please enter the author:")
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        tracks = []
        for record in csv_reader:
            track = (record[0], record[1])
            tracks.append(track)
        
        return (title, author, tracks)
    
def main():
    apollo = album_file("apollo.csv")
    print(apollo)

if __name__ == "__main__":
    main()
