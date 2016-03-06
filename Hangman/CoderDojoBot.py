import sys, time, telepot

class CoderDojoBot(telepot.Bot):
    """Bot class"""

    # Init method. Call init of telepot.Bot
    def __init__(self):
        self.TOKEN = #YOUR_TOKEN#
        super(CoderDojoBot, self).__init__(self.TOKEN)

    # Handle messages and their flavour
    def handle(self, msg):
        pass
