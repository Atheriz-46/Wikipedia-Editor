import tkinter as tk
import Viewer
import FileManager 

class Editor(tk.Frame):
    def Save(self):
        # TODO savebutton pressed 
        pass 

    def changeEditorArticle(self,articleName):
        # TODO Markdown parser call and change contents 
        pass 
          
    def __init__(self, parent,guimanager):
        tk.Frame(self,parent)
        