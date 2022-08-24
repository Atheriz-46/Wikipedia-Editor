from glob import glob
from os.path import join
from FileManager import FileManger

class OpeningPage:
    
    def __init__(self,fileManager):
        self.fm = fileManager

    def generate(self):
        file_list = glob(join(self.fm.currentDirectory,'*.md'))
        content = '# Opening Page \n'
        content = content + '\n'.join(f"- [{name}]({name})" for name in file_list)
        self.fm.saveTo("Homepage.md",content)
