from AskDirectory import AskDirectory 
from GUIManager   import GUIManager

class Bstring:
    directory = ""

directory = Bstring()
ad = AskDirectory(directory)
ad.mainloop()
mainApplication = GUIManager(directory.directory)
mainApplication.mainloop()