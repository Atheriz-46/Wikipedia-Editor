from GUIManager   import GUIManager
import os
import tkinter as tk 
from tkinter import filedialog 
 
iconDirectory = os.path.join(os.getcwd(),"assets","icon.png")
path_work = filedialog.askdirectory() 
if not isinstance(path_work,tuple):
    mainApplication = GUIManager(path_work)
    mainApplication.tk.call('wm', 'iconphoto', mainApplication._w, tk.PhotoImage(file=iconDirectory))
    mainApplication.mainloop()