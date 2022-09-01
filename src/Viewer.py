import tkinter as tk
from MarkdownParser import MarkdownParser

class Viewer(tk.Frame):
    """
    Viewer Frame which shows markdown files extends tk.Frame
	"""
    
    def changeViewerArticle(self,articleName):
        """
        Changes the article currently shown in the Viewer Frame
		Args:
			articleName (str) : Name of the new article to be shown
		"""

        contents = self.manager.fm.fetchFrom(articleName)
        self.textFrame.destroy()
        self.parser.parse(contents)
        self.textFrame = tk.Text(master=self)
        self.textFrame.pack(fill="both",expand=True)
        self.textFrame = self.parser.getFrame(self.textFrame)
        self.textFrame.config(state='disabled')
         
    
    def __init__(self,parent,guimanager):
        """
        Initialization function of Viewer
		Args:
			parent (Frame): Frame to which viewer will be attached to 
            guimanager (GUIManager): Instance of the GUIManager which has created this viewer 
		"""

        tk.Frame.__init__(self,parent)
        self.manager = guimanager
        self.textFrame = tk.Text(master=self)
        self.textFrame.pack(fill="both",expand=True)
        self.parser = MarkdownParser(self)
    
    def link(self,link):
        """
        Handles when links are clicked in Viewer frame
		Args:
			link (str) : Link attached to Hyperlink clicked in Viewer Frame
		"""

        if not self.manager.currentMode==2:
            self.manager.switchToViewer(link.split('/')[-1])
            