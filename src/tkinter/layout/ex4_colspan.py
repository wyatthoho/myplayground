import os
import tkinter as tk

fileDir = os.path.dirname(__file__)
pardir = os.path.abspath(os.path.join(fileDir, os.path.pardir))
logoPath = os.path.join(pardir, 'img', 'w.ico')

root = tk.Tk()
root.title('myApp')
root.geometry('500x200+100+100')
root.resizable(width=0, height=0)
root.iconbitmap(logoPath)

labelFrame1 = tk.LabelFrame(root, text='labelFrame1', height=200, width=500, bg='skyblue')
labelFrame1.grid()

frame1 = tk.Frame(labelFrame1, height=80, width=480, bg='orange')
frame1.grid(row=0, column=0, columnspan=2)

frame3 = tk.Frame(labelFrame1, height=80, width=240, bg='mediumpurple')
frame3.grid(row=1, column=0)

frame4 = tk.Frame(labelFrame1, height=80, width=240, bg='mediumseagreen')
frame4.grid(row=1, column=1)

root.mainloop()