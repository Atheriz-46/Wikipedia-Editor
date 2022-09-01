from glob import glob
from os.path import join

class OpeningPage:
    
    def __init__(self,fileManager):
        self.fm = fileManager

    def generate(self):
        file_list = glob(join(self.fm.currentDirectory,'*.md'))
        content = '# Opening Page \n'
        content = content + '\n'.join(f"- [{name.split('/')[-1][:-3]}]({name})" for name in file_list)
        self.fm.saveTo("HomePage.md",content)
