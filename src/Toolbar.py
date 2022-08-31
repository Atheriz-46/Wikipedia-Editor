import tkinter as tk
from tkinter import ttk


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

		self.btn_back = ttk.Button(master = self, text = " < ", command = self.manager.back)
		self.btn_back.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

		self.btn_home = ttk.Button(master = self, text = "Home", command = self.manager.switchToHomePage)
		self.btn_home.grid(row = 0, column = 1, sticky = 'news')

		self.frm_home = tk.Frame(master = self)
		self.frm_edit = tk.Frame(master = self)
		self.frm_view = tk.Frame(master = self)

		self.btn_render = ttk.Button(master = self.frm_edit, text = "Render", command = (self.manager).frameEditor.render)
		self.btn_render.pack(side = tk.LEFT) 
		self.btn_save = ttk.Button(master = self.frm_edit, text = "Save", command = self.manager.switchToViewer)
		self.btn_save.pack(side = tk.LEFT)

		self.btn_edit = ttk.Button(master = self.frm_view, text = "Edit", command = self.manager.switchToEditor)
		self.btn_edit.pack(side = tk.LEFT)

		self.frm_home.grid(row = 0, column = 2, sticky = "news")
		self.frm_view.grid(row = 0, column = 2, sticky = "news")
		self.frm_edit.grid(row = 0, column = 2, sticky = "news")

# window = tk.Tk()

# tb = Toolbar(window,window)

# tb.pack()


# mainApplication = GUIManager()
# mainApplication.mainloop()