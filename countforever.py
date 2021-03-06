from TwitterAPI import TwitterAPI
from num2words import num2words
from time import sleep

limit = 36  # 100 tweets per hour
ten_minutes = 600  # in seconds
number = 1
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

while True:
    try:
        tweet = "{}{}".format(num2words(number).replace(" and", ""), "...ah ah ah!")
        api.request('statuses/update', {'status': tweet})
        number += 1
        sleep(limit)
    except:
        sleep(ten_minutes)
