import json

# [Chaves e outros tipos de dados]

# Atribuindo os valores de tokens, prefixo, campos e comandos em variáveis
class Key:
	auth = json.loads(open('./json/keys.json', 'r').read())['auth']
	fields = json.loads(open('./json/keys.json', 'r').read())['fields']
	prefix = json.loads(open('./json/keys.json', 'r').read())['prefix']

	commands = json.loads(open('./json/cmd_list.json', 'r').read())['commands']