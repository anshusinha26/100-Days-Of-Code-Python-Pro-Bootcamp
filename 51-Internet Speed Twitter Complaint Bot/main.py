# import the InternetSpeedTwitterComplaintBot class from twitterBot module
from twitterBot import InternetSpeedTwitterComplaintBot

# import the constants from twitterBot module
from twitterBot import PROMISED_DOWN, PROMISED_UP

# created bot object
bot = InternetSpeedTwitterComplaintBot()

# get the net speed
bot.getInternetSpeed()

# variables to store the net speeds
downloadSpeed = bot.down
uploadSpeed = bot.up

# variables to store the promised net speed
promisedDownloadSpeed = PROMISED_DOWN
promisedUploadSpeed = PROMISED_UP

# check if the net speed is less than the promised speed
if downloadSpeed < promisedDownloadSpeed or uploadSpeed < promisedUploadSpeed:
    bot.tweetAtProvider()






