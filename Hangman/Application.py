# Simple Hangman Bot made for the 11th March CoderDojo Master
# Author: Giovanni Riva && Giovanni De Toni
# Mail: giovannimaria.riva at studenti.unitn.it
#       giovanni.detoni at unitn.it

import sys, time, telepot
from telepot.delegate import per_chat_id, create_open
from CoderDojoBot import CoderDojoBot

# Initialize the bot and start the loop
TOKEN = '187053440:AAF199All4GbW5moBpq8tga_SEvQbFNvG88'
bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(CoderDojoBot, timeout=60)),
])
bot.notifyOnMessage(run_forever=True)
