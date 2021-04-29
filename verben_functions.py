# Deutche Verben Spiele - developed for Carolina
# April 2021

import time
import winsound
from ascii_art_text import AsciiArt
from datetime import datetime
from playsound import playsound

def clean_screen():
    for i in range (0,22):
        print('\n')
        time.sleep(.05)


def intro():


    txt_art = AsciiArt("Hello Carolina", 'blue')
    print(txt_art.build_ascii_art())

    txt_art = AsciiArt("Deutche Verben lernen", 'red')
    print(txt_art.build_ascii_art())
    play_sound('intro2.wav')
    #time.sleep(6)


def save_min_to_file(min):
    with open('verben_minuten.txt', 'w') as f:
        now = datetime.now()
        time_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write('Deutsche Verben lernen - V 0.9\n')
        f.write(f'\nyou won {min} minutes on {time_string}\n')
        f.close()


def txt_file_init():
    with open('verben_minuten.txt', 'w') as f:
        now = datetime.now()
        time_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f'\nDeutche Verben Spiele - Session open on: {time_string}\n')
        f.close()


def play_sound(wav):
    playsound(wav)
