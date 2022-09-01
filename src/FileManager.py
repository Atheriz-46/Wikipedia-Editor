"""
Module name : FileManager

Used as a middleman between GUIManager and the file storage system. Sets the home directory, finds files to read from and write to, fetches content of specified files in the home directory.

"""

import os

class FileManager():



	def __init__(self,directory): 

		"""
		Args:
			directory (str) : Sets this as the home directory for the object of FileManager class
		"""

		self.dir = directory
		self.currentDirectory = directory	

	def setDirectory(self, directory): 

		"""
		Used to set the home directory

		Args:
			directory (str) : this is set as the home directory
		"""

		self.dir = directory

	def makeFile(self,articleName):

		"""
		Used to create a new file with name articleName

		Args:
			articleName (str) : the name of the file that has to be created 
		"""

		self.file = open(os.path.join(self.dir,articleName), 'a+')
		self.file.close()
	
	def fetchDirectory(self):

		"""
		Used to get the home directory name / path

		"""

		return self.dir

	def fetchFrom(self, filename):

		"""
		Used to get content from the specified file in the home directory

		Args:
			filename (str) : The file that content has to be fetched from
		"""

		self.file = open(os.path.join(self.dir, filename) , 'r')
		self.content = self.file.read()

		self.file.close()

		return self.content

	def saveTo(self, filename, content):

		"""
		Used to save content to the specified file in the home directory

		Args:
			filename (str) : The name of file in the home directory that content has to saved to
			content (str) : The markdown text that has to be saved to the file
		"""

		self.file = open(os.path.join(self.dir, filename), 'w+')
		self.file.write(content)
		
		self.file.close()

