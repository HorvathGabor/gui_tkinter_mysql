#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-07-06

@author: gaborhorvath
"""

#------------------------------------------------------------------------------
# GUI
#------------------------------------------------------------------------------


# imports
#-------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class basicTab():
    def __init__(self):
        print("hello")
        self.root = ()
        self.tabName = ('test')
        self.tabControl = ttk.Notebook(self.root)
        self.tabOne = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabOne, text = self.tabName)
        self.tabControl.pack(expand = 0)


        
        
# def createWidgets():
#     tabControl = ttk.Notebook(win)
#     tab1 = ttk.Frame(tabControl)
#     tabControl.add(tab1, text='Tab 1')
#     tabControl.pack(expand=1)

    



if __name__ == "__main__":
    win = tk.Tk()                       # Instance of main window
    win.title("Main Python GUI")        # Title
    win.resizable(False, False)           # Enable resizing
    bt = basicTab()
    bt.root = win
    # createWidgets()
    win.mainloop()














# def createWidgets():
#     tabControl = ttk.Notebook(win)
#     tab1 = ttk.Frame(tabControl)
#     tabControl.add(tab1, text='Tab 1')
#     tabControl.pack(expand=1, fill="both")
#     monty = ttk.LabelFrame(tab1, text=' Mighty Python ')
    

# # main 
# #-------------------------------

# win = tk.Tk()                       # Instance of main window
# win.title("Main Python GUI")        # Title
# win.resizable(True, True)           # Enable resizing

# createWidgets()
# win.mainloop()
