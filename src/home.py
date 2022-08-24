from glob import glob
from os.path import join 
class OpeningPage:
    def generate(self,current_directory: str):
        content = None
        glob(join(current_directory,'*.md'))
        saveTo("Homepage.md",content)
