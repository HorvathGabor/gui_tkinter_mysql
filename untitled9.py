#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:49:03 2020

@author: gaborhorvath
"""
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu


#-----------------------------------------------
class Notebook:

    def __init__(self, parent):
        self.root = parent
        self.notebook = ttk.Notebook(self.root)

    def addTab(self,title,text):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text=title)
        
        self.notebook.pack(expand=1, fill="both")
        monty = ttk.LabelFrame(frame, text=' Mighty Python ')
        monty.grid(column=0, row=0, padx=8, pady=4)
        ttk.Label(monty, text="Enter a name:").grid(column=0, row=0,
                                                    sticky='W')
#     name = tk.StringVar()
#     nameEntered = ttk.Entry(monty, width=12, textvariable=name)
#     nameEntered.grid(column=0, row=1, sticky='W')
        
        
        
        
        # label = ttk.Label(frame,text=text)
        # label.grid(column=0,row=0)
        
        # name = tk.StringVar()
        # nameEntered = ttk.Entry(label, width=12, textvariable=name)
        # nameEntered.grid(column=2, row=1, sticky="W")
        
        
        self.notebook.pack()

    # def run(self):
    #     self.root.mainloop()

#======================
win = tk.Tk()
win.title("Python GUI")
win.geometry("900x500")

nb = Notebook(win)
nb.addTab('Frame One','This is on Frame One')
nb.addTab('Frame Two','This is on Frame Two')


#======================
# Start GUI
#======================
win.mainloop()




# def createWidgets():
#     tabControl = ttk.Notebook(win)
#     tab1 = ttk.Frame(tabControl)
#     tabControl.add(tab1, text='Tab 1')
#     tabControl.pack(expand=1, fill="both")
#     monty = ttk.LabelFrame(tab1, text=' Mighty Python ')
#     monty.grid(column=0, row=0, padx=8, pady=4)
#     ttk.Label(monty, text="Enter a name:").grid(column=0, row=0,
#     sticky='W')
#     name = tk.StringVar()
#     nameEntered = ttk.Entry(monty, width=12, textvariable=name)
#     nameEntered.grid(column=0, row=1, sticky='W')
#     action = ttk.Button(monty, text="Click Me!")
#     action.grid(column=2, row=1)
#     ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
#     number = tk.StringVar()
#     numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
#     numberChosen['values'] = (42)
#     numberChosen.grid(column=1, row=1)
#     numberChosen.current(0)
#     scrolW = 30; scrolH = 3
#     scr = scrolledtext.ScrolledText(monty, width=scrolW,
#     height=scrolH, wrap=tk.WORD)
#     scr.grid(column=0, row=3, sticky='WE', columnspan=3)
#     menuBar = Menu(tab1)
#     win.config(menu=menuBar)
#     fileMenu = Menu(menuBar, tearoff=0)
#     menuBar.add_cascade(label="File", menu=fileMenu)
#     helpMenu = Menu(menuBar, tearoff=0)
#     menuBar.add_cascade(label="Help", menu=helpMenu)
#     nameEntered.focus()
#     return tabControl

# # #======================
# win = tk.Tk()
# win.title("Python GUI")
# a = createWidgets()

# createWidgets()
# win.mainloop()