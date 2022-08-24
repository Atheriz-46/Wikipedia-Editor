from errno import errorcode
import tkinter as tk
import Editor 
import Viewer
import Surfer
import OpeningPage 
import FileManager
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

    def handleSubmit(self,ed,wd):
        self.currentDirectory = ed.get()
        wd.destroy()
        
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        # initialize in Homemode 
        self.currentMode = 0
        
        self.sf  = Surfer()

        windowForDirectory = tk.Tk()
        textAskingDirectory = tk.Label(master = windowForDirectory,text="Directory of your library")
        textAskingDirectory.pack(side="left",fill="both",expand=True)
        entryForDirectory = tk.Entry(master = windowForDirectory)
        entryForDirectory.pack(side="right",fill="both",expand=True)
        buttonForDirectory = tk.Button(text="Submit",command=lambda:self.handleSubmit(entryForDirectory,windowForDirectory))
        buttonForDirectory.pack(side="bottom")
        windowForDirectory.mainloop()

        self.op = OpeningPage(self.currentDirectory)
        
        # initialize FileManager
        self.fm = FileManager(self.currentDirectory)

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