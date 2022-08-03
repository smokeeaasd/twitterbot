import importlib
from utils import Key

# [Manipulador de Comandos]
# Classe responsável por validar um comando e executá-lo
class CommandHandler:
	data = None

	def __init__(self, command):
		self.data = command
		for i in Key.commands:
			if f"{self.data}" == f"{Key.prefix} {i}":
				self.data = {
					"is_command": True,
					"command": i
				}
				return
		self.data = {
			"is_command": False
		}
	
	def check_command(self, tweet):
		if (self.data['is_command']):
			importlib.import_module(f"commands.{self.data['command']}").execute(tweet)
		else:
			return