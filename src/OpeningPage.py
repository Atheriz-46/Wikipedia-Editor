from glob import glob
from os.path import join


class OpeningPage:
    """
    Used to create the opening page for the application that lists the files in the home directory
    """
    def __init__(self, fileManager):
        """
        Used to initialise the Opening page and set the fileManager object that handles accessing files

        Args:
                fileManager (FileManager) : Refers to the FileManager object that handles accessing files
        """

        self.fm = fileManager

    def generate(self):
        """
        Used to update the opening page with the list of files in the home directory
        """

        file_list = glob(join(self.fm.currentDirectory, "*.md"))
        content = "# Opening Page \n"
        content = content + "\n".join(
            f"- [{name.split('/')[-1][:-3]}]({name})" for name in file_list
        )
        self.fm.saveTo("HomePage.md", content)
