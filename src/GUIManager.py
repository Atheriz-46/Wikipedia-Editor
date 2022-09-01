import tkinter as tk
from Editor import Editor
from Viewer import Viewer
from Surfer import Surfer
from OpeningPage import OpeningPage
from FileManager import FileManager
from Toolbar import Toolbar


class GUIManager(tk.Tk):
    # Different Modes GUIManager Works in
    # 0 = currently on Homepage
    # 1 = currently Viewing Wiki
    # 2 = currently Editing Wiki

    def deletePage(self):
        """
        Serves toolbar when delete button is pressed in toolbar
        """
        self.fm.delete(self.sf.currentTop())
        self.sf.clear()
        self.switchToHomePage()

    # for backbutton in toolbar
    def newPage(self, articleName):
        """
        Serves toolbar when new page button is pressed in toolbar

        Args:
            articleName (str): Name of the new article to be created
        """

        self.fm.makeFile(articleName)
        self.switchToViewer(articleName)
        self.switchToEditor()

    def back(self):
        """
        Serves toolbar when back button is pressed in toolbar
        """

        self.switchToViewer("back")

    # for switching to editormode
    def switchToEditor(self):
        """
        Internal fuction for switching to editor mode
        """

        self.tb.changeMode(2)
        self.frameEditor.changeEditorArticle(self.sf.currentTop())
        self.frameEditor.tkraise()

    # for switching to an article in viewermode
    def switchToViewer(self, articleName=None):
        """
        Internal fuction for switching to viewer mode showing a given article
        Args:
            articleName (str): Name of the new article to be shown in viewer
        """

        if articleName == None:
            articleName = self.sf.currentTop()
        elif articleName == "back":
            articleName = self.sf.back()
        else:
            self.sf.push(articleName)
        if articleName == "HomePage.md":
            self.tb.changeMode(0)
        else:
            self.tb.changeMode(1)
        self.frameViewer.changeViewerArticle(articleName)
        self.frameViewer.tkraise()

    # for switching to an article in viewermod
    def switchToHomePage(self):
        """
        Internal fuction for switching to go back to Homepage
        """

        self.sf.push("HomePage.md")
        self.tb.changeMode(0)
        self.op.generate()
        self.switchToViewer("HomePage.md")
        self.frameViewer.tkraise()

    def __init__(self, *args, **kwargs):
        """
        Initialization function of GUIManager
        Args:
            directory (str): Name of the directory where the wiki is
        """
        tk.Tk.__init__(self)

        # initialize in Homemode
        self.currentMode = 0
        self.title("WoodooPedia")
        self.sf = Surfer()

        # set directory
        for arg in args:
            self.currentDirectory = arg

        # initialize FileManager
        self.fm = FileManager(self.currentDirectory)
        self.op = OpeningPage(self.fm)

        # initialize topframe
        topFrame = tk.Frame(self)
        topFrame.pack(side="bottom", fill="both", expand=True)

        # initialize toolbar

        # initialize Viewer and Editor
        self.frameViewer = Viewer(topFrame, self)
        self.frameEditor = Editor(topFrame, self)
        topFrame.rowconfigure(0, weight=1)
        topFrame.columnconfigure(0, weight=1)
        self.frameEditor.grid(row=0, column=0, sticky="nsew")
        self.frameViewer.grid(row=0, column=0, sticky="nsew")

        self.tb = Toolbar(self, self)
        self.tb.pack(side="top", fill="both", pady=10)
        self.switchToHomePage()
