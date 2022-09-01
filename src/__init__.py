from AskDirectory import AskDirectory 
from GUIManager   import GUIManager
import os
import tkinter as tk 
class Bstring:
    directory = ""
 
iconDirectory = os.path.join(os.getcwd(),"assets","icon.png")
directory = Bstring()
ad = AskDirectory(directory)
ad.tk.call('wm', 'iconphoto', ad._w, tk.PhotoImage(file=iconDirectory))
ad.mainloop()
mainApplication = GUIManager(directory.directory)
mainApplication.tk.call('wm', 'iconphoto', mainApplication._w, tk.PhotoImage(file=iconDirectory))
mainApplication.mainloop()