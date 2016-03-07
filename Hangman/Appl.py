from CoderDojoBot import CoderDojoBot
import telepot
import sys, time



bot = CoderDojoBot()
while True:
    bot.notifyOnMessage()
    time.sleep(1)
