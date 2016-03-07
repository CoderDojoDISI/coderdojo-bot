import sys, time, telepot
import string

class CoderDojoBot(telepot.Bot):
    """Bot class"""

    # Init method. Call init of telepot.Bot
    def __init__(self):
        self.TOKEN = '187053440:AAF199All4GbW5moBpq8tga_SEvQbFNvG88'
        super(CoderDojoBot, self).__init__(self.TOKEN)
        self.show_keyboard = self.setKeyboard()
        self.choosen_word= 'null'

    ### Handle

    def on_chat_message(self,msg):
        message_type, visibility, user_id = telepot.glance(msg)
        self.user_id = user_id
        message = 'Ciao'
        self.printKeyboard(message)

    ### Game

    # Check if guess belongs to choosen_word

    # Print correct/wrong answer

    # Choose random word from file

    ### Keyboard

    # Print keyboard with given "message"
    def printKeyboard(self,message):
        self.sendMessage(self.user_id, message, reply_markup=self.show_keyboard)

    # Generate keyboard
    def setKeyboard(self):
        alphabetList = list(string.ascii_uppercase)
        first_row = alphabetList[0:6]
        second_row = alphabetList[6:12]
        third_row = alphabetList[12:18]
        fourth_row = alphabetList[18:24]
        fifth_row =  alphabetList[24:27]
        keyboard = {'keyboard': [first_row,second_row,third_row,fourth_row,fifth_row]}
        return keyboard
