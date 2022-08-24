from errno import errorcode
import tkinter
import Editor 
import Viewer
import OpeningPage 
import Toolbar 

class GUIManager:
    currentMode = 0
    op      = OpeningPage()
    tb      = Toolbar()
    # 0 = currently on Homepage
    # 1 = currently Viewing Wiki 
    # 2 = currently Editing Wiki 

    def changeViewerArticle(self,articleName):
        # TODO change viewer here

    def switchPage(self,articleName):
        if self.currentMode == 2:
            # throw an exception to go back to viewerMode first 
            errorcode("Unsafe Switch to ViewerMode") 
        else if self.currentMode == 1:
            if articleName == "Homepage":
                switchToHome()
                changeViewerArticle(articleName)
            else 
                changeViewerArticle(articleName)
        else if self.currentMode == 0:
            if articleName != "Homepage":
                switchToViewer()
                changeViewerArticle(articleName)
        

    def switchToEditor(self):
        self.currentMode = 2
        self.tb.changeMode(2)

    def switchToViewer(self):
        self.currentMode = 1
        self.tb.changeMode(1)

    def switchToHome(self):
        self.currentMode = 0
        op.generate()
        self.tb.changeMode(0)
