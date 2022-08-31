from AskDirectory import AskDirectory 
from GUIManager   import GUIManager

directory = ""
ad = AskDirectory(directory)
ad.mainloop()
print(directory)
mainApplication = GUIManager(directory)
mainApplication.mainloop()