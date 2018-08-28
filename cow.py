from pygame import mixer
import time

while True:
    text = raw_input("Hit return to moo")
    if text == "":
        mixer.init()
    	mixer.music.load('youtubecow.mp3')
    	mixer.music.play()
    	time.sleep(2.5)
    	mixer.music.load('applause.mp3')
    	mixer.music.play()
    	print('Booyaa! Ticket Done')
    	time.sleep(2)