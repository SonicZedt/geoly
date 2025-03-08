import requests

class AWS:
	def checkip(self) -> str:
		response = requests.get('https://checkip.amazonaws.com/')

		if(not response.ok):
			return ""
		
		return response.text.strip()