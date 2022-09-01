import tkinter as tk
from tkinter import ttk


class Toolbar(tk.Frame):
	
	def changeMode(self, newMode):

		"""
		Used to change the widgets displayed on Toolbar depending on mode. Called by GUIManager

		Args:
			newMode (int) : Specifies the mode to be switched to - {0 : Home mode, 1 : View mode, 2 : Edit mode}

		"""

		if (newMode == 0):
			self.frm_home.tkraise()

		elif (newMode == 1):
			self.frm_view.tkraise()

		elif (newMode == 2):
			self.frm_edit.tkraise()


	def __init__(self, parent, guimanager):

		"""
		Initialises all frames and widgets for Toolbar

		Args:
			parent (tk.Tk) : The parent window where the toolbar frame is to be displayed
			guimanager (GUIManager) : Used to link the Toolbar to GUIManager object

		"""

		tk.Frame.__init__(self, master = parent, relief = tk.SUNKEN, borderwidth = 1)

		self.manager = guimanager

		self.btn_back = ttk.Button(master = self, text = " < ", command = self.manager.back)
		self.btn_back.grid(row = 0, column = 0, sticky = "news")

		self.btn_home = ttk.Button(master = self, text = "Home", command = self.manager.switchToHomePage)
		self.btn_home.grid(row = 0, column = 1, sticky = 'news')

		self.frm_home = tk.Frame(master = self)
		self.frm_edit = tk.Frame(master = self)
		self.frm_view = tk.Frame(master = self)

		self.btn_render = ttk.Button(master = self.frm_edit, text = "Save", command = (self.manager).frameEditor.render)
		self.btn_render.pack(side = tk.LEFT) 
		self.btn_save = ttk.Button(master = self.frm_edit, text = "Exit", command = self.manager.switchToViewer)
		self.btn_save.pack(side = tk.LEFT)

		self.btn_edit = ttk.Button(master = self.frm_view, text = "Edit", command = self.manager.switchToEditor)
		self.btn_edit.pack(side = tk.LEFT)

		self.ent_home = tk.Entry(master = self.frm_home)
		self.btn_new_home = ttk.Button(master = self.frm_home, text = "New Page", command = lambda: self.newPage(self.frm_home))

		self.ent_view = tk.Entry(master = self.frm_view)
		self.btn_new_view = ttk.Button(master = self.frm_view, text = "New Page", command = lambda: self.newPage(self.frm_view))

		self.btn_new_home.pack(side = tk.RIGHT)
		self.ent_home.pack(side = tk.RIGHT)

		self.btn_new_view.pack(side = tk.RIGHT)
		self.ent_view.pack(side = tk.RIGHT)

		self.columnconfigure(2, weight = 1)

		self.frm_home.grid(row = 0, column = 2, sticky = "news")
		self.frm_view.grid(row = 0, column = 2, sticky = "news")
		self.frm_edit.grid(row = 0, column = 2, sticky = "news")

	def newPage(self, frm):

		"""
		Used to create a new Page. Called when "New Page" button is clicked. Fetches new page name from entry widget and call newPage() from GUIManager

		Args:
			frm (tk.Frame) : Specifies the mode in which the "New Page" button has been clicked {frm_home : Home mode, frm_view : View mode}

		"""

		if (frm == self.frm_home):
			self.manager.newPage(self.ent_home.get())
			self.ent_home.delete(0,tk.END)

		elif(frm == self.frm_view):
			self.manager.newPage(self.ent_view.get())
			self.ent_view.delete(0,tk.END)

# window = tk.Tk()

# tb = Toolbar(window,window)

# tb.pack()


# mainApplication = GUIManager()
# mainApplication.mainloop()