import tkinter as tk
from Viewer import Viewer


class Editor(tk.Frame):
    def render(self):
        """
        Renders the Editor Frame
        """
        fileContent = self.txtFrame.get("1.0", tk.END)
        self.manager.fm.saveTo(self.manager.sf.currentTop(), fileContent)
        self.vw.changeViewerArticle(self.manager.sf.currentTop())

    def changeEditorArticle(self, articleName):
        """Changes active article to articleName

        Args:
            articleName (str): Name of the article to be edited
        """
        self.vw.changeViewerArticle(articleName)
        self.txtFrame.delete("1.0", tk.END)
        self.txtFrame.insert("1.0", self.manager.fm.fetchFrom(articleName))

    def __init__(self, parent, guimanager):

        tk.Frame.__init__(self, parent)
        self.manager = guimanager
        self.primeFrame = tk.Frame(self)
        self.txtFrame = tk.Text(master=self.primeFrame, wrap="word")
        self.vw = Viewer(self.primeFrame, guimanager)
        self.txtFrame.pack(side="left", fill="both", expand=True)
        self.vw.pack(side="right", fill="both", expand=True)
        self.primeFrame.pack(side="bottom", fill="both", expand=True)
