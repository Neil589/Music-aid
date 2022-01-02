from lyrics_extractor import SongLyrics
from tkinter import *
from numpy import integer
from spotipy import *
import pandas as pd
import spotipy
from random import randint
from spotipy.oauth2 import SpotifyClientCredentials

# initialize spotify client credentials
cid = '8151af96b02d42c9801c4f189f7334a9'
secret = '31bf22a14cda421898fc18ac714c75e4'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

# make track attribute arrays
artist_name = []
track_name = []
popularity = []

# get popular artists,tracks and popularity for each artist
for i in range(0,1000,50):
    track_results = sp.search(q='year:2021', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        popularity.append(t['popularity'])


# clear function to remove label text
def clear_widget_text(widget):
    widget.destroy()

#get lyrics function- uses GCS API KEY and GCS ENGINE ID to retrieve wanted lyrics from input from genius.com
def get_lyrics():
    extract_lyrics = SongLyrics("AIzaSyDYxm7BSo2ScHWBjhkCeTbRkUBH8qRI5DM","baf4c9b4758d46256")
    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    result.set(res)
    
#modified get lyrics function that generates a random track    
def get_rand_lyrics():
    extract_lyrics = SongLyrics("AIzaSyDYxm7BSo2ScHWBjhkCeTbRkUBH8qRI5DM","baf4c9b4758d46256")
    i = randint(0,1000)
    temp = extract_lyrics.get_lyrics(str(track_name[i]))
    res = temp['lyrics']
    result.set(res)
    # disp2 = Label(master, text="Song: " + track_name[i], textvariable=track_name[i],
    #   bg="light grey").grid(row=2, column=1, rowspan=1)
    # T = Text(master, "Song: " + track_name[i]).grid(row=2, column=1)

    textBox = Entry(master)
    textBox.insert(0, "Song: " + track_name[i])
    textBox.pack
    
    disp3 = Label(master, text="Artist: " + artist_name[i], textvariable=artist_name[i],
      bg="light grey").grid(row=3, column=1, rowspan=1)
    # clear_widget_text(disp2)
    # clear_widget_text(disp3)
 
# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='light grey')
boxy = Grid()

#Scroll bar implementation
scroll = Scrollbar(master)
 
# Variable Classes in tkinter
result = StringVar()
 
# Creating label for each information
# name using widget Label
song_name = Label(master, text="Enter Song name : ",
      bg="light grey").grid(row=0)

# Creating label for class variable
# name using widget Entry
disp = Label(master, text="", textvariable=result,
      bg="light grey").grid(row=4, column=1)

e = Entry(master, width=50)
e.grid(row=0, column=1)
 
# a button using the widget
b = Button(master, text="Show",
           command=get_lyrics, bg="Blue")
 
b.grid(row=0, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5,)

# Random button
c = Button(master, text="Random",
           command=get_rand_lyrics, bg="Blue")
c.grid(row=0, column=4, columnspan=2,
       rowspan=2, padx=5, pady=5,)

scroll_bar = Scrollbar(master)
 
mainloop()