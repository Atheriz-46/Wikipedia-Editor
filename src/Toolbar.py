import tkinter as tk

# class GUIManager(tk.Tk):
#     # Different Modes GUIManager Works in 
#     # 0 = currently on Homepage
#     # 1 = currently Viewing Wiki 
#     # 2 = currently Editing Wiki 
    
#     # def back(self):
#     #     self.switchToViewer("back")

#     def switchToEditor(self):
        
#         self.tb.changeMode(2)
#         # self.frameViewer.changeEditorArticle(self.sf.currentTop())
#         # self.frames[Editor].tkraise()
    
#     def switchToViewer(self,articleName=None):

#         # if articleName == None:
#         #     articleName = self.sf.currentTop()
#         # elif articleName == "back":
#         #     articleName = self.sf.back()
#         # else :
#         #     self.sf.push(articleName)
        
#         self.tb.changeMode(1)
#         # self.frameViewer.changeViewerArticle(articleName)
#         # self.frameViewer.tkraise()

#     def switchToHomePage(self):
        
#         # self.sf.push("HomePage")
#         self.tb.changeMode(0)
#         # self.op.generate()
#         # self.switchToViewer("HomePage")
#         # self.frames[Viewer].tkraise()

#     # def handleSubmit(self,ed,wd):
#     #     self.currentDirectory = ed.get()
#     #     wd.destroy()
        
#     def __init__(self,*args,**kwargs):
#         tk.Tk.__init__(self,*args,**kwargs)
        
#         # initialize in Homemode 
#         self.currentMode = 0
        
#         # self.sf  = Surfer()

#         # self.windowForDirectory = tk.Tk()
#         # textAskingDirectory = tk.Label(master = windowForDirectory,text="Directory of your library")
#         # textAskingDirectory.pack(side="left",fill="both",expand=True)
#         # entryForDirectory = tk.Entry(master = windowForDirectory)
#         # entryForDirectory.pack(side="right",fill="both",expand=True)
#         # buttonForDirectory = tk.Button(text="Submit",command=lambda:self.handleSubmit(entryForDirectory,windowForDirectory))
#         # buttonForDirectory.pack(side="bottom")
#         # windowForDirectory.mainloop()

#         # self.op = OpeningPage(self.currentDirectory)
        
#         # initialize FileManager
#         # self.fm = FileManager(self.currentDirectory)

#         #initialize toolbar 
#         self.tb = Toolbar(self, self)
#         self.tb.pack(master = self, side="top",fill="both",expand=True)

#         #initialize Viewer and Editor
#         # topFrame = tk.Frame(self)
#         # self.frameViewer = Viewer(topFrame, self)
#         # self.frameEditor = Editor(topFrame, self)
#         # self.switchToHomePage()
#         # topFrame.pack(side="bottom",fill="both",expand=True)
#         self.mainloop()


class Toolbar(tk.Frame):

	def changeMode(self, newMode):
		if (newMode == 0):
			self.frm_home.tkraise()

		elif (newMode == 1):
			self.frm_view.tkraise()

		elif (newMode == 2):
			self.frm_edit.tkraise()

	def __init__(self, parent, guimanager):

		tk.Frame.__init__(self, master = parent, relief = tk.SUNKEN, borderwidth = 1)

		self.manager = guimanager

		self.btn_back = tk.Button(master = self, text = " < ", command = self.manager.back())
		self.btn_back.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

		self.btn_home = tk.Button(master = self, text = "Home", command = self.manager.switchToHomePage)
		self.btn_home.grid(row = 0, column = 1, sticky = 'news')

		self.frm_home = tk.Frame(master = self)
		self.frm_edit = tk.Frame(master = self)
		self.frm_view = tk.Frame(master = self)

		self.btn_render = tk.Button(master = self.frm_edit, text = "Render", command = self.manager.frameEditor.render())
		self.btn_render.pack(side = tk.LEFT) 
		self.btn_save = tk.Button(master = self.frm_edit, text = "Save", command = self.manager.switchToViewer)
		self.btn_save.pack(side = tk.LEFT)

		self.btn_edit = tk.Button(master = self.frm_view, text = "Edit", command = self.manager.switchToEditor)
		self.btn_edit.pack(side = tk.LEFT)

		self.frm_home.grid(row = 0, column = 2, sticky = "news")
		self.frm_view.grid(row = 0, column = 2, sticky = "news")
		self.frm_edit.grid(row = 0, column = 2, sticky = "news")

# window = tk.Tk()

# tb = Toolbar(window,window)

# tb.pack()


# mainApplication = GUIManager()
# mainApplication.mainloop()