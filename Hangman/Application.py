# Simple Hangman Bot made for the 11th March CoderDojo Master
# Author: Giovanni Riva && Giovanni De Toni
# Mail: giovannimaria.riva at studenti.unitn.it
#       giovanni.detoni at unitn.it

import sys, time, telepot
from CoderDojoBot import CoderDojoBot

# Initialize the bot and start the loop
bot = CoderDojoBot()
bot.notifyOnMessage()
while True:
    time.sleep(1)
