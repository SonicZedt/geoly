import json
import os
import dotenv
import base64
import requests
import io
import logging
from oauth2client.service_account import ServiceAccountCredentials

dotenv.load_dotenv()

def __parse_json_structure(str: str):
	config_dict = dict(json.loads(str))
	config = {}

	for param in config_dict['parameters'].keys():
		if config_dict['parameters'][param]['valueType'] != "JSON":
			continue

		config[param] = json.loads(config_dict['parameters'][param]['defaultValue']['value'])

	return json.dumps(config, indent=2)

def update_from_remote():
	# print('[Config] Setting up configuration')

	# remote_config_url = ''
	# service_account = json.loads(base64.b64decode(os.getenv('SERVICE_ACCOUNT')).decode("utf-8"))
	# access_token = ServiceAccountCredentials.from_json_keyfile_dict(
	#     keyfile_dict=service_account,
	#     scopes=['https://www.googleapis.com/auth/firebase.remoteconfig']
	# ).get_access_token().access_token

	# headers = { 'Authorization': f'Bearer {access_token}' }
	# response = requests.get(remote_config_url, headers=headers)

	# try:
	#     print('[Config] Trying to update configuration')
	#     if response.status_code == 200:
	#         with io.open('./bot/config.json', 'wb') as f:
	#             f.write(__parse_json_structure(response.text).encode('utf-8'))

	#         print('[Config] Remote config retrieved, config updated')
	#         print('[Config] ETag from server: {}'.format(response.headers['ETag']))
	#     else:
	#         print('[Config] Unable to get remote config, using default config')
	#         print(f'[Config] {response.text}')
	# except Exception as e:
	#     print('[Config] Something wrong when updating configuration')
	#     print(f'[Config] {e}')
	
	return json.load(open('./bot/config.json'))

config = update_from_remote()
release = os.getenv('RELEASE')
token = os.getenv('DEV_TOKEN') if release == 'DEV' else os.getenv('PROD_TOKEN')


class Logging:
	write = config['logging']['write']
	level = config['logging']['level']
	write_to_channel = config['logging']['writeToChannel']


class Guild:
	id = config['guild']['id']
	channel_log_ip = config['guild']['channelLogIp']