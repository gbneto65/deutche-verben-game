# Deutche Verben Spiele - developed for Carolina
# April 2021
# version 0.8

import pyfiglet
from termcolor import colored


class AsciiArt:

    def __init__(self, ascii_text, text_color):
        self.ascii_text = ascii_text
        self.text_color = text_color

    def build_ascii_art(self):
        ascii_verben = pyfiglet.figlet_format(self.ascii_text)
        colored_ascii_verben = colored(ascii_verben, self.text_color)
        return colored_ascii_verben

