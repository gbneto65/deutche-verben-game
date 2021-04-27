import datetime
import time
import winsound
from ascii_art_text import AsciiArt


def clean_screen():
    print('\n' * 22)

# Deutche Verben Spiele - developed for Carolina
# April 2021
from datetime import datetime

def intro():
    winsound.PlaySound('intro2.wav', winsound.SND_ASYNC)
    txt_art = AsciiArt("Hello Carolina", 'blue')
    print(txt_art.build_ascii_art())

    txt_art = AsciiArt("Deutche Verben lernen", 'red')
    print(txt_art.build_ascii_art())

    time.sleep(6)


def save_min_to_file(min):
    with open('verben_minuten.txt', 'a') as f:
        now = datetime.now()
        time_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f'\nyou won {min} minutes on {time_string}\n')
        f.close()


def txt_file_init():
    with open('verben_minuten.txt', 'w') as f:
        now = datetime.now()
        time_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f'\nDeutche Verben Spiele - Session open on: {time_string}\n')
        f.close()
