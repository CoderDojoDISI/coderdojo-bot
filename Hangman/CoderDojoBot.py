# Simple Hangman Bot made for the 11th March CoderDojo Master
# Author: Giovanni Riva && Giovanni De Toni
# Mail: giovannimaria.riva at studenti.unitn.it
#       giovanni.detoni at studenti.unitn.it

import sys, time, telepot
import string
from os.path import getsize
from random import randint

class CoderDojoBot(telepot.helper.ChatHandler):
    """Bot class"""

    # Init method. Call init of telepot.Bot and set up some
    # useful game variables.
    def __init__(self, seed_tuple, timeout):
        super(CoderDojoBot, self).__init__(seed_tuple, timeout)
        self.keyboard = self.setKeyboard()
        self.hiddenWord = []            # Word print representation
        self.choosen_word = []          # Word that has to be found by the user
        self.lives = 8                  # Total game lives
        self.heart = u'\u2764\ufe0f'    # Heart emoj unicode
        self.gameOn = False

    ### Handle
    # Method that will be called when a message is recived by the bot
    def on_message(self,msg):
        if (msg['text'] == "/start"):
            self.beginGame()
            self.printKeyboard(self.printHiddenWord()+"\nGuess a letter!\n"+self.printHearts())
        elif self.gameOn == True:
            self.findGuess(msg['text'])
            if (self.completeHiddenWord()):
                hide_keyboard = {'hide_keyboard': True}
                self.printKeyboard(self.printHiddenWord()+'\n'+self.printHearts())
                self.sender.sendMessage("You win!. Write /start if you want to play again!", reply_markup=hide_keyboard)
                self.gameOn = False
            else:
                if (self.isAlive()):
                    self.printKeyboard(self.printHiddenWord()+'\n'+self.printHearts())
                else:
                    hide_keyboard = {'hide_keyboard': True}
                    self.sender.sendMessage("You lost!. Write /start if you want to play again!", reply_markup=hide_keyboard)
                    self.gameOn = False

    ### Game
    # Find guessed letter(s) in hidden_word. It will also remove
    # the choosen letter from the keyboard.
    def findGuess(self,msg):
        found = False
        for i in range(0,len(self.choosen_word)):
            if (str(msg).lower() == self.choosen_word[i] and self.hiddenWord[i] == '_'):
                self.hiddenWord[i] = str(msg)
                found = True
        if (not found):
            self.removeLife()
        self.removeFromKeyboard(str(msg))


    # Start the game after /start command
    def beginGame(self):
        self.gameOn = True
        self.regenValues()
        self.sender.sendMessage("The game will begin now!")
        self.choosen_word = 'cazzomene'#list(self.generateWord())
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

    # Check if guess belongs to choosen_word
    def printHiddenWord(self):
        return " ".join(self.hiddenWord)

    # Print hearts
    def printHearts(self):
        totalLives = ""
        for i in range(0, self.lives):
            totalLives += self.heart + " "
        return totalLives

    # Check if hidden_word is complete
    def completeHiddenWord(self):
        for i in range(0,len(self.hiddenWord)):
            if (self.hiddenWord[i] == '_'):
                return False
        return True

    # Choose random word from file
    def generateWord(self):
        dic_path ="DictionaryE.txt"
        file_size =getsize (dic_path )
        file_in =open (dic_path ,"rb")
        while True :
            offset =randint (0 ,file_size )
            file_in .seek (offset )
            L =file_in .read (25 ).split ("\r\n")
            if len (L )>2 :
                return L [1 ]

    ### Keyboard
    # Print keyboard with given "message"
    def printKeyboard(self,message):
        self.sender.sendMessage(message, reply_markup=self.keyboard)

    # Generate keyboard
    def setKeyboard(self):
        alphabetList = list(string.ascii_uppercase)
        first_row = alphabetList[0:6]
        second_row = alphabetList[6:12]
        third_row = alphabetList[12:18]
        fourth_row = alphabetList[18:24]
        fifth_row =  alphabetList[24:27]
        return {'keyboard': [first_row,second_row,third_row,fourth_row,fifth_row]}

    # Remove a letter from the keyboard
    def removeFromKeyboard(self, letter):
        for i in range(0,len(self.keyboard['keyboard'])):
            for j in range(0, len(self.keyboard['keyboard'][i])):
                if (self.keyboard['keyboard'][i][j] == letter):
                    return self.keyboard['keyboard'][i].pop(j)
