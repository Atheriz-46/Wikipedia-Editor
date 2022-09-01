from ids import MarkdownParser
import tkinter as tk

sample_md = "This will be the [basic](sample\link) building block of our IDS. The structure needs to be such that there is easy translation from md to ids and ids to the tkinter frame. Since only one direction of the transformation is required, this makes the choice of structure, linear or nested, for the IDS, important. Since we need to finally get a tkinter object, we\n## H1 check ***bold check*** *italics check* \n\n* bi\n\t* bi"

window = tk.Tk()
parser = MarkdownParser()
parser.parse(sample_md)
print(str(parser.root))
##parser is correct


frame = parser.getFrame(window)
frame.pack()

window.mainloop()