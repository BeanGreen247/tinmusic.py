#sudo apt install python3-tk python3-dev python3
#python3 -m pip install pygame
#to run the app run as follows
#
#python3 tinmusic.py
#

#Bugs
#Emotes cause app to crash if present in file name

#things to work on
#add mp3 and flac support

#with the next 2 lines uses about 13MB of RAM
#from tkinter import *
#from pygame import *

#with the next 2 lines uses about 11MB of RAM
from tkinter import Button, Tk, Entry, Listbox, ACTIVE, SINGLE, END
from pygame import mixer
import pygame
import os

root = Tk()
root.title("tinmusic")
root.resizable(width=False, height=False)

e = Entry(root, text = "100")

def playsong():
    currentsong = playlist.get(ACTIVE)
    mixer.init()
    mixer.music.load(currentsong)
    mixer.music.play()

def playsongonloop():
    currentsong = playlist.get(ACTIVE)
    mixer.init()
    mixer.music.load(currentsong)
    mixer.music.play(-1)

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()

def changedirectory():
    os.chdir(playlist.get(ACTIVE))
    playlist.delete(0,END)
    song = os.listdir()
    for s in song:
        playlist.insert(END,s)

def musichomedirectory():
    os.chdir(f'/home/{username}/Music')
    playlist.delete(0,END)
    song = os.listdir()
    for s in song:
        playlist.insert(END,s)

def setvolume():
    volumeval = float(int(e.get())/100)
    mixer.music.set_volume(volumeval)

Button(root,text = "open folder", command = changedirectory).grid(row = 1, column = 0)
Button(root,text = "music dir", command = musichomedirectory).grid(row = 1, column = 1)
Button(root,text = "play", command = playsong).grid(row = 1, column = 2)
Button(root,text = "play on loop", command = playsongonloop).grid(row = 1, column = 3)
Button(root,text = "pause", command = pausesong).grid(row = 1, column = 4)
Button(root,text = "resume", command = resumesong).grid(row = 1, column = 5)
Button(root,text = "stop", command = stopsong).grid(row = 1, column = 6)
e.grid(row = 1, column = 7)
Button(root,text = "set volume", command = setvolume).grid(row = 1, column = 8)

pygame.init()
mixer.init()
playlist = Listbox(root, selectmode=SINGLE, height = 20, width = 100, selectbackground = "blue", selectforeground = "white")
playlist.grid(columnspan = 85)
playlist.delete(0,END)
username = os.getlogin()
os.chdir(f'/home/{username}/Music')
song = os.listdir()
for s in song:
    playlist.insert(END,s)

root.mainloop()
