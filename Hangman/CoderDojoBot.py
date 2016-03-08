# Simple Hangman Bot made for the 11th March CoderDojo Master
# Author: Giovanni Riva && Giovanni De Toni
# Mail: giovannimaria.riva at studenti.unitn.it
#       giovanni.detoni at unitn.it

import sys, time, telepot
import string
from os.path import getsize
from random import randint

class CoderDojoBot(telepot.Bot):
    """Bot class"""

    # Init method. Call init of telepot.Bot and set up some
    # useful game variables.
    def __init__(self):
        self.TOKEN = '187053440:AAF199All4GbW5moBpq8tga_SEvQbFNvG88'
        super(CoderDojoBot, self).__init__(self.TOKEN)
        self.keyboard = self.setKeyboard()
        self.hiddenWord = []            # Word print representation
        self.choosen_word = ""          # Word that has to be found by the user
        self.choosen_word_list = []     # Word representation as a list
        self.lives = 8                  # Total game lives
        self.heart = u'\u2764\ufe0f'    # Heart emoj unicode

    ### Handle
    # Method that will be called when a message is recived by the bot
    def on_chat_message(self,msg):
        message_type, visibility, user_id = telepot.glance(msg)
        self.user_id = user_id
        if (msg['text'] == "/start"):
            self.beginGame()
            self.printKeyboard(self.printMessage()+"\nGuess a letter!\n"+self.printHearts())
        else:
            if (self.isAlive()):
                if (not(self.completeHiddenWord())):
                    self.findGuess(msg['text'])
                    self.printKeyboard(self.printMessage()+'\n'+self.printHearts())
                else:
                    hide_keyboard = {'hide_keyboard': True}
                    self.sendMessage(self.user_id, "You win! Bitch!. Write start if you want to play again!", reply_markup=hide_keyboard)
            else:
                hide_keyboard = {'hide_keyboard': True}
                self.sendMessage(self.user_id, "You lost! Bitch!. Write start if you want to play again!", reply_markup=hide_keyboard)

    ### Game
    # Find guessed letter(s) in hidden_word. It will also remove
    # the choosen letter from the keyboard.
    def findGuess(self,msg):
        found = False
        for i in range(0,len(self.choosen_word_list)):
            if (str(msg).lower() == self.choosen_word_list[i]):
                self.hiddenWord[i] = str(msg)
                found = True
        if (not found):
            self.removeLife()
        self.removeFromKeyboard(str(msg))


    # Start the game after /start command
    def beginGame(self):
        self.regenValues()
        self.sendMessage(self.user_id, "The game will begin now!")
        self.choosen_word = self.generateWord()
        self.choosen_word_list = list(self.choosen_word)
        for i in range(0,len(self.choosen_word_list)):
            self.hiddenWord.append("_ ")

    # Regenerate the default game values (for a new game)
    def regenValues(self):
        self.keyboard = self.setKeyboard()
        self.hiddenWord = []
        self.choosen_word = ""
        self.choosen_word_list = []
        self.lives = 7
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
    def printMessage(self):
        message = ""
        for v in self.hiddenWord:
            message += v
        return message

    # Print hearts
    def printHearts(self):
        totalLives = ""
        for i in range(0, self.lives):
            totalLives += self.heart + " "
        return totalLives

    # Check if hidden_word is complete
    def completeHiddenWord(self):
        for i in range(0,len(self.hiddenWord)):
            if (self.hiddenWord[i] == '_ '):
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
        self.sendMessage(self.user_id, message, reply_markup=self.keyboard)

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
