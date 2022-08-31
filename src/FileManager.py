# saveTo
# fetchFrom
# setDirectory
# fetchDirectory

import os

class FileManager():
	
	def __init__(self,directory): 
		self.dir = directory
		self.currentDirectory = directory	
	def setDirectory(self, directory): 
		self.dir = directory

	def fetchDirectory(self):
		return self.dir

	def fetchFrom(self, filename):
		self.file = open(os.path.join(self.dir, filename) , 'r')
		self.content = self.file.read()

		self.file.close()

		return self.content

	def saveTo(self, filename, content):
		self.file = open(os.path.join(self.dir, filename), 'w')
		self.file.write(content)
		
		self.file.close()

