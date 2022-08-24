from errno import errorcode
import tkinter as tk
import Editor 
import Viewer
import Surfer
import OpeningPage 
import Toolbar    

class GUIManager(tk.Tk):
    # Different Modes GUIManager Works in 
    # 0 = currently on Homepage
    # 1 = currently Viewing Wiki 
    # 2 = currently Editing Wiki 
    
    def back(self):
        self.switchToViewer("back")

    def switchToEditor(self):
        
        self.tb.changeMode(2)
        self.frameViewer.changeEditorArticle(self.sf.currentTop())
        self.frames[Editor].tkraise()
    
    def switchToViewer(self,articleName=None):

        if articleName == None:
            articleName = self.sf.currentTop()
        elif articleName == "back":
            articleName = self.sf.back()
        else :
            self.sf.push(articleName)
        
        self.tb.changeMode(1)
        self.frameViewer.changeViewerArticle(articleName)
        self.frameViewer.tkraise()

    def switchToHomePage(self):
        
        self.sf.push("HomePage")
        self.tb.changeMode(0)
        self.op.generate()
        self.switchToViewer("HomePage")
        self.frames[Viewer].tkraise()

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        # initialize in Homemode 
        self.currentMode = 0
        
        self.sf  = Surfer()

        #TODO current Directory diolougue
        self.currentDirectory = "" 
        
        self.op = OpeningPage(self.currentDirectory)
        
        #initialize toolbar 
        tb = Toolbar(self)
        tb.pack(side="top",fill="both",expand=True)

        #initialize Viewer and Editor
        topFrame = tk.Frame(self)
        self.frameViewer = Viewer(topFrame, self)
        self.frameEditor = Editor(topFrame, self)
        self.switchToHomePage()
        topFrame.pack(side="bottom",fill="both",expand=True)

mainApplication = GUIManager()
mainApplication.mainloop()