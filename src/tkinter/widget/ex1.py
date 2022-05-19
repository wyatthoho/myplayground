import os
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk


def ClickBtn1():
    msg = 'button 1 is clicked'
    strVar1.set(msg)


def ClickBtn2(msg):
    strVar1.set(msg)


def ClickBtn3():
    strVar1.set('')


def ClickChkBtn1():
    if boolVar1.get():
        fontStyle['weight'] = 'bold'
    else:
        fontStyle['weight'] = 'normal'


def ClickChkBtn2():
    if boolVar2.get():
        fontStyle['slant'] = 'italic'
    else:
        fontStyle['slant'] = 'roman'


def ChangeFamily():
    if radioValue.get() == 1:
        fontStyle['family'] = 'Arial'
    else:
        fontStyle['family'] = 'Calibri'


def ChangeColor(*args):
    label1['fg'] = combobox1.get()
    frame1.focus()


# Path settings
fileDir = os.path.dirname(__file__)
pardir = os.path.abspath(os.path.join(fileDir, os.path.pardir))
logoPath = os.path.join(pardir, 'img', 'w.ico')
imgPath = os.path.join(pardir, 'img', 'btn.png')

# root
root = tk.Tk()
root.title('myApp')
root.geometry('500x200+100+100')
root.resizable(width=0, height=0)
root.iconbitmap(logoPath)

# frame 1
frame1 = tk.LabelFrame(root, text='Print messages', width=450, height=50)
frame1.grid(row=0, column=0,padx=5, pady=5, columnspan=3, sticky=tk.W)
frame1.grid_propagate(0)

strVar1 = tk.StringVar()
fontStyle = tkFont.Font(family='Helvetica', size=11, weight='normal', slant='roman')
label1 = tk.Label(master=frame1, bg='white', width=45, height=1, textvariable=strVar1, font=fontStyle)
label1.grid(row=0, column=0, padx=5, pady=5)

# frame 2
frame2 = tk.LabelFrame(root, text='Buttons')
frame2.grid(row=1, column=0, padx=5, pady=5, rowspan=3, sticky=tk.NW)

btn1 = tk.Button(frame2, text='btn1', width=15, command=ClickBtn1)
btn1.grid(row=0, column=0, padx=5, pady=5)
# configs = btn1.configure().keys()
# print(configs)

btn2 = tk.Button(frame2, text='btn2', width=15, command=lambda: ClickBtn2('button 2 is clicked'))
btn2.grid(row=1, column=0, padx=5, pady=5)

image = tk.PhotoImage(file=imgPath)
btn3 = tk.Button(frame2, text='btn3', image=image, width=40, height=40, command=ClickBtn3)
btn3.grid(row=0, column=1, rowspan=2, padx=5, pady=5, ipadx=10, ipady=10)

# frame 3
frame3 = tk.LabelFrame(root, text='Bold / Italic')
frame3.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NW)

boolVar1 = tk.BooleanVar()
checkBtn1 = tk.Checkbutton(frame3, text='Bold', var=boolVar1, command=ClickChkBtn1)
checkBtn1.grid(row=0, column=0, padx=5, pady=5)

boolVar2 = tk.BooleanVar()
checkBtn2 = tk.Checkbutton(frame3, text='Italic', var=boolVar2, command=ClickChkBtn2)
checkBtn2.grid(row=0, column=1, padx=5, pady=5)

# frame 4
frame4 = tk.LabelFrame(root, text='Font family')
frame4.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NW)

radioValue = tk.IntVar()
radioBtn1 = tk.Radiobutton(frame4, text='Arial', variable=radioValue, value=1, command=ChangeFamily)
radioBtn1.grid(row=0, column=0, padx=5, pady=5)

radioBtn2 = tk.Radiobutton(frame4, text='Calibri', variable=radioValue, value=2, command=ChangeFamily)
radioBtn2.grid(row=0, column=1, padx=5, pady=5)
radioValue.set(1)

# frame 5
frame5 = tk.LabelFrame(root, text='Font color')
frame5.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NW)

values = ['black', 'green', 'blue']
combobox1 = ttk.Combobox(frame5, width=8, values=values, state='readonly')
combobox1.grid(row=0, column=0, padx=5, pady=5)
combobox1.current(0)
combobox1.bind("<<ComboboxSelected>>", ChangeColor)
root.mainloop()

