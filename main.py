import tkinter as tk
import lexicon_gui



win = tk.Tk()

win.title("Map Words To Sentences")
win.geometry("740x420") 
win.resizable(0, 0) 


myGUI = lexicon_gui.LexGUI(win)

myGUI.createGUI()


win.mainloop()