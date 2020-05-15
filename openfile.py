import tkinter as tk
import datetime
from PIL import Image
from tkinter import filedialog
from tkinter.ttk import *

root = tk.Tk()

root.call('wm', 'attributes', '.', '-topmost', True)
today = datetime.datetime.today()
namefile= today.strftime("%Y-%m-%d-%H%M%S")+str('.pdf')
def open_file(): 
    files = filedialog.askopenfilename(multiple=True) 
    var = root.tk.splitlist(files)
    filePaths = []
    for f in var:
        filePaths.append(f)
    filePaths
    Table=[]
    for i in range(len( filePaths)):
        Table.append(Image.open( filePaths[i]))
    """def Der():
         val=Table.pop(0)
         Tables=Table
         return Tables
      
    Data=Der()"""
    Table[0].save(namefile,'PDF',resolution=100.0,save_all=1,append_images=Table)
 
button =tk.Button(root,text="votre fichier",command=open_file)
button.pack()
root.mainloop()