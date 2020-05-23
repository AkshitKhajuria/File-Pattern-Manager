#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.1
#  in conjunction with Tcl version 8.6
#    May 21, 2020 06:49:18 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import patternEditor

class Pattern_Widget:
    
    pat_type = ""
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.types = {0:"String", 1:"Number"} #Good for some book keeping
        self.pat_type = 0   #this variable holds the currently equipped pattern
        self.lock = 1   #A lock to make sure only one Editor window is opened per button

        self.pattern_button = tk.Button(self.frame, text="String", width=10, command=self.new_window)
        self.pattern_button.pack(fill=tk.BOTH, expand=True)
        self.frame.pack(fill=tk.Y, side=tk.LEFT, padx=2, pady=4)

    def new_window(self):
        
        def on_closing():
            #Release lock
            self.lock = 1
            #Close window
            self.newWindow.destroy()
        
        if(self.lock):
            #Set lock
            self.lock = 0
            self.newWindow = tk.Toplevel(self.master)
            #Open editor window
            self.app = patternEditor.Editor(self.newWindow, self)
            self.newWindow.protocol("WM_DELETE_WINDOW", on_closing)


    def set_type(self, t):
        # The type of pattern can be 0 for "String" or 1 for "Number"
        self.pat_type = t
        self.pattern_button.configure(text=self.types[t])      


class Toplevel1:

    def addPattern(self, master):
        if (self.no_patterns>3):
            print("Number of patterns limited to 4!")
            return None
        self.no_patterns = self.no_patterns+1
        Pattern_Widget(master)

    def create_button_clicked(self):
        #   Logic for creating patterns
        #   Patterns need to follow the pattern criteria set by user
        #   A Pattern can be a set of numbes and/or strings
        #   While strings are constant, number patterns will loop from start[user ip, default=1]
        #   to end[user ip, def=10]
        #   with step[also user ip, def=1]
        #   For eg: A patter starting with string "Larry" followed by numbers 1-5
        #   So we need to make 5 dirs with names "Larry1", "Larry2", .... "Larry5"
        #   Create a list of such pattern strings and then make dirs with names in that list
        print("Oops! Someone has been lazy!")


    def __init__(self, top=None):
        self.no_patterns = 0
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+650+150")
        top.minsize(176, 1)
        top.maxsize(1924, 1050)
        top.resizable(1, 1)
        top.title("File Pattern Manager")
        top.configure(background="#d9d9d9")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.05, rely=0.089, relheight=0.278
                , relwidth=0.917)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''File Pattern''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.4, rely=0.422, height=52, width=128)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Pattern''')
        self.Button1.configure(command= lambda: self.addPattern(self.Labelframe1))

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.6, height=41, width=137)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Target Directory''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.317, rely=0.622,height=26, relwidth=0.64)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.383, rely=0.844, height=42, width=148)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Create''')
        self.Button2.configure(command=self.create_button_clicked)


if __name__ == '__main__':
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

