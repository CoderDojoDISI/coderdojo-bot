import sys, time, telepot
import string

class CoderDojoBot(telepot.Bot):
    """Bot class"""

    # Init method. Call init of telepot.Bot
    def __init__(self):
        self.TOKEN = '187053440:AAF199All4GbW5moBpq8tga_SEvQbFNvG88'
        super(CoderDojoBot, self).__init__(self.TOKEN)


    def handle(self, msg):
        flavor = telepot.flavor(msg)

        if flavor == 'normal':
            message_type, visibility, user_id = telepot.glance(msg)
            show_keyboard = self.setKeyboard()
            self.sendMessage(user_id, 'This is a custom keyboard', reply_markup=show_keyboard)
        else:
            raise telepot.BadFlavour(msg)

    def setKeyboard(self):
        alphabetList = list(string.ascii_uppercase)
        first_row = alphabetList[0:6]
        second_row = alphabetList[6:12]
        third_row = alphabetList[12:18]
        fourth_row = alphabetList[18:24]
        fifth_row =  alphabetList[24:27]
        keyboard = {'keyboard': [first_row,second_row,third_row,fourth_row,fifth_row]}
        #keyboard = {'keyboard': [['Yes','No']]}
        return keyboard
