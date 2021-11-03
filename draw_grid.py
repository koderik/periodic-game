from tkinter import *

ws = Tk()
ws.title('Sfärdudie')
ws.geometry('1200x600')
ws.config(bg='#fff')

canvas = Canvas(ws, height=600, width=1200, bg="#fff")

canvas.pack()

canvas.create_rectangle(30, 30, 80, 80, outline="#fff", fill="#fb0")



for x in range(9):
    for y in range(18):


ws.mainloop()