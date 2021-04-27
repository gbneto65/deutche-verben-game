# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:11:00 2021

@author: BRGUBO
"""
import time
import pandas as pd
import random
from datetime import datetime
import winsound
import sys
import pyfiglet



def clean_screen():
    print('\n'*25)

def intro():
    winsound.PlaySound('intro.wav', winsound.SND_ASYNC)
    ascii_intro_banner = pyfiglet.figlet_format("Hello Carolina")
    print(ascii_intro_banner)
    ascii_intro_banner2 = pyfiglet.figlet_format("Deutche Verben")
    print(ascii_intro_banner2)
    time.sleep(12)


def save_min_to_file(min):
    with open('verben_minuten.txt' , 'a') as f:
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
df_rows = len(verb_df)-1
min = 0
txt_file_init()
intro()

while True:
    
    clean_screen()
    rnd_row =random.randint(0, df_rows)
    rnd_choose = verb_df.iloc[rnd_row].values.tolist()
    print(f'Du hast {min} Minuten un Minecraft zu spielen ')

    ascii_verben = pyfiglet.figlet_format(rnd_choose[0])
    print(ascii_verben)

    print(f'\nDie Verb ist: {rnd_choose[0]}\n')
    ans = input(f'{rnd_choose[1]} ')
    
    if ans == rnd_choose[2]:

        winsound.PlaySound('right_sound.wav', winsound.SND_ASYNC)

        print(f'Korrect!!! - {rnd_choose[1]} {rnd_choose[2]}')
        print('')
        min = min + .5
        input('Waiter - Drucken etwas')
    
    elif ans == str(99):
        save_min_to_file(min)
        print('Bis Bald!!!')
        break
    
    else:
        winsound.PlaySound('wrong_sound.wav', winsound.SND_ASYNC)
        ascii_verben = pyfiglet.figlet_format('Nein!')
        print(ascii_verben)

        print('Leider nicht Korrect')
        print(f'{rnd_choose[1]} {rnd_choose[2]}')
        min = min -1
        input('Drucken etwas')
        


    
    



