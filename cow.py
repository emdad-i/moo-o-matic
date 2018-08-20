import keyboard #Using module keyboard
from playsound import playsound #Using module playsound

while True:#making a loop
	if keyboard.is_pressed('enter'):
		playsound('youtubecow.mp3')
		print('Booyaa! Ticket Done')
			