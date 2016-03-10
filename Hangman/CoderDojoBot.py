# Simple Hangman Bot made for the 11th March CoderDojo Master
# Author: Giovanni Riva && Giovanni De Toni
# Mail: giovannimaria.riva at studenti.unitn.it
#       giovanni.detoni at studenti.unitn.it

import sys, time, telepot, string
from os.path import getsize
from random import randint
from CoderDojoClass import CoderDojoBotClass

class CoderDojoBot(CoderDojoBotClass):
    """Bot class"""

    # Init method. Call init of telepot.Bot and set up some
    # useful game variables.
    def __init__(self, seed_tuple, timeout):
        super(CoderDojoBot, self).__init__(seed_tuple, timeout)

    # Start the game after /start command
    def beginGame(self):
        self.gameOn = True
        self.regenValues()
        self.sender.sendMessage("The game will begin now!")
        self.choosen_word = list(self.generateWord())
        for i in range(0,len(self.choosen_word)):
            self.hiddenWord.append("_")

    # Regenerate the default game values (for a new game)
    def regenValues(self):
        self.keyboard = self.setKeyboard()
        self.hiddenWord = []
        self.choosen_word = []
        self.lives = 8
        self.heart = u'\u2764\ufe0f'

    # Remove one player life
    def removeLife(self):
        self.lives -= 1

    #Check if player has enough life to play
    def isAlive(self):
        if (self.lives >= 1):
            return True
        else:
            return False

    # Generate keyboard
    def setKeyboard(self):
        alphabetList = list(string.ascii_uppercase)
        first_row = alphabetList[0:6]
        second_row = alphabetList[6:12]
        third_row = alphabetList[12:18]
        fourth_row = alphabetList[18:24]
        fifth_row =  alphabetList[24:27]
        return {'keyboard': [first_row,second_row,third_row,fourth_row,fifth_row]}
