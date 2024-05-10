from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("textfile","*.txt")))
print (root.filename)