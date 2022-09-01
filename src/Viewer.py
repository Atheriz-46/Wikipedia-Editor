import tkinter as tk
from MarkdownParser import MarkdownParser

class Viewer(tk.Frame):
    def changeViewerArticle(self,articleName):
        # TODO Markdown parser call and change contents 
        contents = self.manager.fm.fetchFrom(articleName)
        self.textFrame.destroy()
        # self.textFrame.config(state='normal')
        # for tag in self.textFrame.tag_names():
            # self.textFrame.tag_remove(tag, 1.0, tk.END)
        # self.textFrame.delete('1.0',tk.END)
        self.parser.parse(contents)
        self.textFrame = tk.Text(master=self)
        self.textFrame.pack(fill="both",expand=True)
        self.textFrame = self.parser.getFrame(self.textFrame)
        self.textFrame.config(state='disabled')
         
    
    def __init__(self,parent,guimanager):
        tk.Frame.__init__(self,parent)
        self.manager = guimanager
        self.textFrame = tk.Text(master=self)
        self.textFrame.pack(fill="both",expand=True)
        self.parser = MarkdownParser(self)
    
    def link(self,link):
        if not self.manager.currentMode==2:
            self.manager.switchToViewer(link.split('/')[-1])
            