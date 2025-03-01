import requests
from json import *

class main:
	def __init__(self):
		self.url = 'http://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency.json'
		
	def getinfo(self):
		self.info = requests.request('get', self.url)
		self.file1 = self.info.json()
		# print(file)
		with open('Gold.json', 'a') as file:
			dump(self.file1, file, indent=4)

obj = main()

obj.getinfo()






