import tkinter as tk
class AskDirectory(tk.Tk): 
    def handleSubmit(self):
        self.str.directory = self.entryForDirectory.get()
        self.destroy()

    def __init__(self,txt):
        tk.Tk.__init__(self)
        self.str = txt 
        self.title("Enter Directory of Wiki")
        self.textAskingDirectory = tk.Label(master = self,text="Directory of your library")
        self.textAskingDirectory.pack(side="left",fill="both",expand=True)
        self.entryForDirectory = tk.Entry(master = self)
        self.entryForDirectory.pack(side="right",fill="both",expand=True)
        self.buttonForDirectory = tk.Button(master = self,text="Submit",command=lambda:self.handleSubmit())
        self.buttonForDirectory.pack(side="bottom")