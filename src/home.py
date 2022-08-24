from FileManager import FileManager
from glob import glob
from os.path import join 
class OpeningPage:
    def __init__(self,current_directory:str ):
        self.current_directory = current_directory
    def generate(self,):
        file_list = glob(join(self.current_directory,'*.md'))
        content = '# Opening Page \n'
        content = content + '\n'.join(f"- [{name}]({name})" for name in file_list)
        FileManager.saveTo("Homepage.md",content)
