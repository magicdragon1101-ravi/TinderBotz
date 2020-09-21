'''
Created by Frederikme (TeetiFM)
Examples of usage are demonstrated in this quickstart.py file
'''

from bot import *
import constants
import random

email = constants.email
password = constants.password

if __name__ == "__main__":

    # creates instance of bot
    bot = TinderBot()

    # login using your google account
    bot.loginUsingGoogle(email=email, password=password)

    # start scraping as much geomatches as possible
    while True:

        # get user
        geomatch = bot.getGeomatch()
        print(geomatch.getDictionary())

        # account is scraped, now dislike and go next (since dislikes are infinite)
        bot.dislike(amount=1)

        # make a random sleep between dislikes between 0 and 2 seconds so it it looks human-like behaviour
        sleepy_time = random.random() * 2
        time.sleep(sleepy_time)
