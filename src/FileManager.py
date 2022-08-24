class FileManger:
    
    def fetchFrom(self,articleName):
        # TODO return contents of that file 
        pass 
    
    def saveTo(self,articleName):
        # TODO saves contents to that file 
        pass 
    
    def setDirectory(self,directory):
        self.currentDirectory = directory
    
    def __init__(self,directoryName):
        self.setDirectory(directoryName)