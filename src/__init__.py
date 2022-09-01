from GUIManager   import GUIManager
import os
import tkinter as tk 
from tkinter import PhotoImage, filedialog 
 
iconDirectory = os.path.join(os.getcwd(),"assets","icon.png")
path_work = filedialog.askdirectory(initialdir='./') 
path_work = os.path.relpath(path_work,os.getcwd())
mainApplication = GUIManager(path_work)
mainApplication.mainloop()