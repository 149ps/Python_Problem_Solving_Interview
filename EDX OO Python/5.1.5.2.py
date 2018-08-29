class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#Write your code here!
common=Artist("Taylor Swift","Big Machine Records, LLC")
song_1=Song("You Belong With Me","Fearless",2008,common)
song_2=Song("All Too Well","Red",2012,common)
song_3= Song("Up We Go","Midnight Machines",2016,Artist("LiGHTS","Warner Bros. Records Inc."))

print("Song_1: " + song_1.artist.name + song_1.artist.label)
print("song_2: " + song_2.artist.name + song_2.artist.label)