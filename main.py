import os
import sys
import random
import time
import multiprocessing

import art # external library to print ASCII-art, if not available print text normally
import playsound # external library to play music, if not available music will not play

# import helper functions
from randomColorGenerator import randomColorSelector
from ASCIIArtGenerator import ASCIIArtGenerator
from clearScreen import clearScreen

def textColorSwitcher(message:str):
    """
        Switches the color of the input string at regular intervals.
    """
    try:
        message = ASCIIArtGenerator(message)
    except NameError:
        """Please install the python 'art' library to display the message in ASCII-art format.\nCommand:
        pip install art \nIf not installed, text will appear in standard format
        """

    while True:
        time.sleep(0.1)
        clearScreen()
        sys.stdout.write(randomColorSelector() + message)
        sys.stdout.flush()

def playMusic(musicPath:str):
    try:
        playsound.playsound(musicPath)
    except NameError:
        """Please install the audio module 'playsound' to play audio.\nCommand:
        pip install playsound\nIf not install, program will be played without audio.
        """    

def run(message, musicPath):
    processTextDisplay = multiprocessing.Process(target=textColorSwitcher, args=[message])
    processMusic = multiprocessing.Process(target=playMusic,args=[musicPath])

    processTextDisplay.start()
    processMusic.start()

    # wait for the music to end and terminate the program
    processMusic.join()
    if not processMusic.is_alive():
        processTextDisplay.terminate()


message = "Happy Birthday,\n Sandesh Dai!"
musicPath = "audio/Fur-Elise-10-Second.m4a"

run(message,musicPath)

