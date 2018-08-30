from pygame import mixer
import time
import os, random

path = 'sounds/animals'

def filePicker():
    file = random.choice(os.listdir(path))
    r = path+'/'+file
    return r

print('---Moo-O-Matic---')
print('---Started---')

while True:
    text = raw_input('Hit return key')
    if text == '':
        mixer.init()
    	mixer.music.load(filePicker())
    	mixer.music.play()
    	time.sleep(2.5)
    	mixer.music.load('sounds/applause.mp3')
    	mixer.music.play()
    	print('Booyaa! Ticket Done')
    	time.sleep(2)