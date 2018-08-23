import keyboard #Using module keyboard
from pygame import mixer
import time

while True:#making a loop
	if keyboard.is_pressed('enter'):
		mixer.init()
		mixer.music.load('youtubecow.mp3')
		mixer.music.play()
		print('Booyaa! Ticket Done')
		time.sleep(1) 