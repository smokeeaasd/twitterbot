import tweepy

from authentication import Login
from utils import Key
from commands.command_handler import CommandHandler

app = Login.app
api = Login.api

# [Classe Principal]
# Responsável por tratar os principais métodos e passar comandos para a classe CommandHandler
class Application(tweepy.StreamingClient):
	def on_connect(self):
		print(f"Conectado!")

	def on_tweet(self, tweet):
		if 'referenced_tweets' in tweet.data:
			return

		app.like(tweet.data['id'])
		data = CommandHandler(tweet.text)
		data.check_command(tweet)

# Inicializando a instância da classe com o token de portador da API do Twitter
# responsável por inicializar a stream
client = Application(Key.auth['BEARER_TOKEN'])

# Adicionar regras de filtragem, assim, apenas os tweets contendo a string serão passados para o Application.on_tweet():
# client.add_rules(tweepy.StreamRule("@exoduscu"))

# Obtendo as regras de filtragem
print(client.get_rules())

# StreamingClient.filter -> filtrando a Stream, com base nas regras de amostra e campos
client.filter(
	tweet_fields=Key.fields['tweet_fields'],
	user_fields=Key.fields['user_fields']
)