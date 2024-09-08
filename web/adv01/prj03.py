from tkinter import *
import sys
import os

# 設定工作目錄
os.chdir(sys.path[0])
windows = Tk()
windows.title("my  gui")

canvas = Canvas(windows, width=500, height=500, bg="white")  # 建立畫布
canvas.pack()  # 將畫布放入windows

# 設定視窗圖片
windows.iconbitmap("crocodile2.ico")
# 載入圖片
img = PhotoImage(file="crocodile2.gif")
myimg = canvas.create_image(250, 250, image=img)
mainloop()
