from pygame import mixer
import time
import os, random

path = 'sounds/animals'

def filePicker():
    file = random.choice(os.listdir(path))
    r = path+'/'+file
    return r

print('---Moo-O-Matic---')
print('Improving team morale')
print('---Started---')

while True:
    text = raw_input('Hit return key')
    if text == '':
        mixer.init()
    	mixer.music.load(filePicker())
    	mixer.music.play()
    	while True:
            if 0 == mixer.music.get_busy():
                mixer.music.load('sounds/applause.mp3')
                mixer.music.play()
                print('Booyaa! Ticket Done')
                break