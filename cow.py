from pygame import mixer
import time
import os

path = 'sounds/animals'
l = os.listdir(path)
x = 0

def sequence():
    global x
    name = ""
    if x < len(l):
        name = path+'/'+l[x]
        x += 1
    else:
        x = 1
        return path+'/'+l[0]
        
    return name

print('---Moo-O-Matic---')
print('Improving team morale')
print('---Started---')

while True:
    text = raw_input('Hit return key')
    if text == '':
        mixer.init()
    	mixer.music.load(sequence())
    	mixer.music.play()
    	while True:
            if 0 == mixer.music.get_busy():
                mixer.music.load('sounds/applause.mp3')
                mixer.music.play()
                print('Booyaa! Ticket Done')
                break