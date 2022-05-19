import os
import tkinter as tk

fileDir = os.path.dirname(__file__)
pardir = os.path.abspath(os.path.join(fileDir, os.path.pardir))
logoPath = os.path.join(pardir, 'img', 'w.ico')

root = tk.Tk()
root.title('myApp') # 設定視窗名稱
root.geometry('500x200+100+100') # 設定視窗大小及位置(width x height + x + y)
root.resizable(width=0, height=0) # 決定能用滑鼠拖曳來改變多少的視窗大小
root.iconbitmap(logoPath)
root.mainloop() # 啟用視窗

