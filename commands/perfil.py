from utils import Key
from authentication import Login

app = Login.app

def execute(tweet):
	author_id = tweet.data['author_id']

	user = app.get_user(id=author_id, user_fields=Key.fields['user_fields']).data
	
	title = f"❓ Informações sobre @{user.username}:"

	seguidores = f" 🔹 Seguidores: {user.public_metrics['followers_count']}"
	seguindo = f" 🔹 Seguindo: {user.public_metrics['following_count']}"

	tweet_count = f" 🔹 Tweets: {user.public_metrics['tweet_count']}"
	
	perfil = f"{title}\n{seguidores}\n{seguindo}\n{tweet_count}"

	app.create_tweet(in_reply_to_tweet_id=tweet.data['id'], text=perfil)