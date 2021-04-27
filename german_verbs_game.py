# Deutche Verben Spiele - developed for Carolina
# April 2021
# version 0.9

import time
import pandas as pd
import random
from datetime import datetime
import winsound
import sys
import pyfiglet
# ascii_font ='3-d'
from termcolor import colored

from ascii_art_text import AsciiArt


def clean_screen():
    print('\n' * 25)


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


verb_df = pd.read_excel('german_verbs.xlsx', header=0)
df_rows = len(verb_df) - 1
min = 0
txt_file_init()
intro()

while True:

    clean_screen()
    rnd_row = random.randint(0, df_rows)
    rnd_choose = verb_df.iloc[rnd_row].values.tolist()
    print(f'Du hast {min} Minuten un Minecraft zu spielen ')

    txt_art = AsciiArt(rnd_choose[0], 'yellow')
    print(txt_art.build_ascii_art())

    print(f'\nDie Verb ist: {rnd_choose[0]}\n')
    ans = input(f'{rnd_choose[1]} ')

    if ans == rnd_choose[2]:
        winsound.PlaySound('right_sound.wav', winsound.SND_ASYNC)

        txt_art = AsciiArt('sehr gut', 'green')
        print(txt_art.build_ascii_art())

        print(f'\n  {rnd_choose[1]} {rnd_choose[2]}')
        print('')
        min = min + .5
        input('Drucken etwas zu weitermachen')

    elif ans == str(99):
        save_min_to_file(min)
        print('Bis Bald!!!')
        break

    else:
        winsound.PlaySound('wrong_sound.wav', winsound.SND_ASYNC)

        txt_art = AsciiArt('Nein', 'red')
        print(txt_art.build_ascii_art())

        txt_art = AsciiArt(f'{rnd_choose[1]}  {rnd_choose[2]}', 'blue')
        print(txt_art.build_ascii_art())

        # ascii_answer = pyfiglet.figlet_format(f'{rnd_choose[1]} {rnd_choose[2]}')
        # colored_ascii_answer = colored(ascii_answer, 'blue')
        # print(colored_ascii_answer)

        print('*** Leider das ist nicht Korrect ***')
        print(f'\n Das richtige ist:  {rnd_choose[1]} {rnd_choose[2]}')
        min = min - 1
        input('\nDrucken etwas zu weitermachen')


