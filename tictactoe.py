import tkinter as tk
from tkinter import messagebox
from tkinter import *

window = tk.Tk()
frame = Frame(window)
frame.pack()
click = True
def clear():
    global click
    click = True
    button1.config(text="  ")
    button2.config(text="  ")
    button3.config(text="  ")
    button4.config(text="  ")
    button5.config(text="  ")
    button6.config(text="  ")
    button7.config(text="  ")
    button8.config(text="  ")
    button9.config(text="  ")
def btnclick(button):
    global click
    if(button['text'] == "  " and click == True):
         button.config(text="X")
         click = False
         checkwin()
    elif(button['text'] == "  " and click == False):
        button.config(text="O")
        click = True
        checkwin()
button1 = tk.Button(frame,text="  ",command=lambda: btnclick(button1),width="10",height="5")
button1.grid(row = 0,column =0)
button2 = tk.Button(frame,text="  ",command=lambda: btnclick(button2),width="10",height="5")
button2.grid(row = 0,column =1)
button3 = tk.Button(frame,text="  ",command=lambda: btnclick(button3),width="10",height="5")
button3.grid(row = 0,column =2)
button4 = tk.Button(frame,text="  ",command=lambda: btnclick(button4),width="10",height="5")
button4.grid(row = 1,column = 0)
button5 = tk.Button(frame,text="  ",command=lambda: btnclick(button5),width="10",height="5")
button5.grid(row = 1,column = 1)
button6 = tk.Button(frame,text="  ",command=lambda: btnclick(button6),width="10",height="5")
button6.grid(row = 1,column = 2)
button7 = tk.Button(frame,text="  ",command=lambda: btnclick(button7),width="10",height="5")
button7.grid(row = 2,column = 0)
button8 = tk.Button(frame,text="  ",command=lambda: btnclick(button8),width="10",height="5")
button8.grid(row = 2,column = 1)
button9 = tk.Button(frame,text="  ",command=lambda: btnclick(button9),width="10",height="5")
button9.grid(row = 2,column = 2)
def checkwin():
    if(button1['text'] != "  "):
        if(button1['text'] == button2['text'] and button2['text'] == button3['text']):
            if(button1['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button4['text'] != "  "):
        if (button4['text'] == button5['text'] and button5['text'] == button6['text']):
            if (button4['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button7['text'] != "  "):
        if (button7['text'] == button8['text'] and button8['text'] == button9['text']):
            if (button7['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button1['text'] != "  "):
        if (button1['text'] == button4['text'] and button4['text'] == button7['text']):
            if (button1['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button2['text'] != "  "):
        if (button2['text'] == button5['text'] and button5['text'] == button8['text']):
            if (button2['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button3['text'] != "  "):
        if (button3['text'] == button6['text'] and button6['text'] == button9['text']):
            if (button3['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button1['text'] != "  "):
        if (button1['text'] == button5['text'] and button5['text'] == button9['text']):
            if (button1['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
    if (button3['text'] != "  "):
        if (button3['text'] == button5['text'] and button5['text'] == button7['text']):
            if (button3['text'] == "X"):
                messagebox.showinfo("x win","X win")
                clear()
            else:
                messagebox.showinfo("o win","O win")
                clear()
window.mainloop()
