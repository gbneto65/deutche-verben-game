# Deutche Verben Spiele - developed for Carolina
# April 2021
# version 0.9

import sys
import time
import pandas as pd
import random
from datetime import datetime
import winsound
from ascii_art_text import AsciiArt
from verben_functions import txt_file_init, intro, clean_screen, save_min_to_file

data = 'german_verbs.xlsx'

try:
    verb_df = pd.read_excel(data, header=0)
except OSError:
    print(f'Could not read database {data}')
    sys.exit()

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
        clean_screen()
        txt_art = AsciiArt(f'Bye Carol', 'blue')
        print(txt_art.build_ascii_art())
        save_min_to_file(min)
        print('Bis Bald!!!')
        break

    else:
        winsound.PlaySound('wrong_sound.wav', winsound.SND_ASYNC)

        txt_art = AsciiArt('Nein', 'red')
        print(txt_art.build_ascii_art())

        txt_art = AsciiArt(f'{rnd_choose[1]}  {rnd_choose[2]}', 'blue')
        print(txt_art.build_ascii_art())

        print('*** Leider das ist nicht Korrect ***')
        print(f'\n Das richtige ist:  {rnd_choose[1]} {rnd_choose[2]}')
        min = min - 1
        input('\nDrucken etwas zu weitermachen')


