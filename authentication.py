import tweepy
from utils import Key

# [Autenticação do Cliente]
# 
class Login:
	# tweepy.Client permite utilizar os endpoints da versão 2 da API do Twitter
	app = tweepy.Client(
			Key.auth['BEARER_TOKEN'],

			Key.auth['CONSUMER_KEY'],
			Key.auth['CONSUMER_SECRET'],

			Key.auth['ACCESS_TOKEN'],
			Key.auth['ACCESS_TOKEN_SECRET']
	)

	_auth = tweepy.OAuth1UserHandler(
		Key.auth['CONSUMER_KEY'],
		Key.auth['CONSUMER_SECRET'],
		Key.auth['ACCESS_TOKEN'],
		Key.auth['ACCESS_TOKEN_SECRET'])

	# tweepy.API permite utilizar os endpoints da versão 1.1 da API do Twitter
	api = tweepy.API(_auth)