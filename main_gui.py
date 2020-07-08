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

#======================
# Global variables
#======================




#===============================================
# Create notebook class with widget functions
#===============================================
class Notebook:
    """Create a notebook"""
    def __init__(self, master=None):
        self.root = master
        self.notebook = ttk.Notebook(self.root)

        
        s = ttk.Style()
        s.configure('Red.TLabelframe.Label', background='blue')

    #-----------------------------------------------
    def addTab(self, title):
        """Create new tab"""
        self.new_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.new_frame, text=title)
        self.notebook.pack(expand=True, fill="both", padx=2, pady=2)
    
    #-----------------------------------------------
    def addLabelFrame(self, title):
        """Add label frame to the new tab"""
        self.new_label_frame = ttk.LabelFrame(self.new_frame, text=title)
        self.new_label_frame.grid(column=0, row=0, padx=100, pady=20)
        
    #-----------------------------------------------
    def addLabel(self, text):
        """Add label to label frame"""
        self.new_label = ttk.Label(self.new_label_frame,
                                   text=text+":").grid(column=0, row=0)
        # Add entry field
        name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.new_label_frame, width=12,
                                     textvariable=name)
        self.nameEntered.grid(column=1, row=0)
        
        
        
        
        # label = ttk.Label(frame,text=text)
        # label.grid(column=0,row=0)
        
        # name = tk.StringVar()
        # nameEntered = ttk.Entry(label, width=12, textvariable=name)
        # nameEntered.grid(column=2, row=1, sticky="W")
        
        
        self.notebook.pack()

#-----------------------------------------------



#==========================
# Create instance of window
#==========================
win = tk.Tk()
win.title("Python GUI")
win.geometry("900x500+100+100")
win.maxsize(1000, 600)
win.minsize(900, 500)
win.configure(background="blue")

#==========================
# Create instance of notebook
#==========================
nb = Notebook(win)

#==========================
# Create instance of notebook
#==========================
# First tab
tab1 = "Tab one"
inputFields = ["First name"]
nb.addTab(tab1)
nb.addLabelFrame(tab1)
nb.addLabel(inputFields[0])

#-----------------------------------------------
# Second tab
tab2 = "Tab two"
inputFields = ["Layer name"]
nb.addTab(tab2)
nb.addLabelFrame(tab2)
nb.addLabel(inputFields[0])

print(nb.__dict__)

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