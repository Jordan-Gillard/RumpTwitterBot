import tweepy, time
from credentials import *
import glob

def send(tweets):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)

	#get images that were generated
	images = glob.glob("trump_exec_order_*")

	for index, tweet in enumerate(tweets):
		try:
			api.update_with_media(images[index], "#MAGA #AmericaFirst #FakeNews @realDonaldTrump")
		except tweepy.TweepError as e:
			log.log(e)
