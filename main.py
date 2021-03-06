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
from tkinter import filedialog, scrolledtext, messagebox
import os

no_patterns = 0
max_patterns = 4
pattern_list = []

class Pattern_Widget:
    
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.editor = patternEditor.Editor(self)

        self.pattern_button = tk.Button(self.frame, text="String", width=10, command=self.open_editor)
        self.pattern_button.bind("<Button-3>", self.remove_pattern)
        self.pattern_button.pack(fill=tk.BOTH, expand=True, padx=2, pady=4)
        self.frame.pack(fill=tk.Y, side=tk.LEFT)

    
    def remove_pattern(self, event):
        self.frame.destroy()
        global no_patterns
        no_patterns = no_patterns-1
        global pattern_list
        pattern_list.remove(self)
        del self


    def open_editor(self):
        
        def on_closing():
            #Close window
            self.newWindow.grab_release()
            self.newWindow.destroy()
        
        #Set the button disabled. We want only one editor for a pattern button
        # self.pattern_button.configure(state="disabled")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.grab_set()
        #Open editor window
        self.editor.show_Editor(self.newWindow)
        self.newWindow.protocol("WM_DELETE_WINDOW", on_closing)

    def set_button_text(self, t:str):
        # The type of pattern can be 0 for "String" or 1 for "Number"
        self.pattern_button.configure(text=t)      


class Toplevel1:

    def addPattern(self):
        global no_patterns, max_patterns, pattern_list
        if (no_patterns>max_patterns-1):
            messagebox.showinfo(title="Max Patterns", message="Number of patterns limited to {}.".format(max_patterns))
            return None
        no_patterns = no_patterns+1
        x=Pattern_Widget(self.Labelframe1)
        pattern_list.append(x)

    def create_button_clicked(self):
        '''  Logic for creating patterns
          Patterns need to follow the pattern criteria set by user
          A Pattern can be a set of numbes and/or strings
          While strings are constant, number patterns will loop from start[user ip, default=1]
          to end[user ip, def=10]
          with step[also user ip, def=1]
          For eg: A patter starting with string "Larry" followed by numbers 1-5
          So we need to make 5 dirs with names "Larry1", "Larry2", .... "Larry5"
          Create a list of such pattern strings and then make dirs with names in that list
          While the above example sounds simple, we can have patterns with multiple numeric
          patterns. These patterns need to run like a click counter with strings appearing in between
          correctly; Not so trivial task now, is it? ''' 
        
        global pattern_list, no_patterns
        #empty pattern check
        if(no_patterns==0):
            messagebox.showinfo(title="Empty pattern", message="No patterns to create.")
            return
        #Initilize the list with the first pattern.
        generated_patterns = pattern_list[0].editor.get_pattern()

        for i in pattern_list[1:]: 
            '''Concatinate every element in generated_patterns list with the next pattern 
            Then replace the generated_patterns list with this new list. Every pattern sequence is 
            built upon previously generated patterns. I know a tree could be used for better understandable
            code, but that means adding tons of more code. Plus this is more efficient.'''
            i_ = i.editor.get_pattern()
            tmp = []
            for j in i_:
                x = (element+j for element in generated_patterns)
                tmp.extend(x)
            generated_patterns = tmp
        
        if len("".join(generated_patterns))==0:
            messagebox.showinfo(title="Empty pattern", message="No patterns to create.")
            return
        else:
            for dirName in (self.target_dir+"/"+i for i in generated_patterns):
                if not os.path.exists(dirName):
                    os.mkdir(dirName)
                    print("Directory :" , dirName ,  " created.")
                else:    
                    print("Directory :" , dirName ,  " already exists. Skipping.")
        # print(generated_patterns)

    def get_target_dir(self):
        '''Get the target directory path where you want to create/edit files. The is not updated if 
        no directory is selected'''
        d = filedialog.askdirectory()
        if d=="":
            # if messagebox.askretrycancel(title="Warning", message="You have not selected a directory.\nRetry?"):
            #     self.get_target_dir()
            pass
        else:    
            self.target_dir = d
            # print("Seleted :" , self.target_dir)
            self.myentry.configure(state='normal')
            self.myentry.delete(0,tk.END)
            self.myentry.insert(0, self.target_dir)
            self.myentry.configure(state='readonly')    

    def __init__(self, top:tk.Tk):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        #The target path where you want to created/edit files.
        self.target_dir = os.getcwd()

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
        self.Button1.configure(command= self.addPattern)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.05, rely=0.6, height=41, width=137)
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(text='''Target Directory''')
        self.Button3.configure(command = self.get_target_dir)

        #This little widget displays the selected target directory 
        #in a horizontally scrollable text entry
        self.myframe = ttk.Frame(top)
        self.myentry = ttk.Entry(self.myframe)
        self.myscroll = ttk.Scrollbar(self.myframe, orient='horizontal', command=self.myentry.xview)
        self.myentry.config(xscrollcommand=self.myscroll.set)
        self.myentry.insert(0, self.target_dir)
        self.myentry.configure(state='readonly')

        self.myframe.place(relx=0.317, rely=0.622,height=37, relwidth=0.64)
        self.myentry.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.myscroll.pack(side=tk.TOP, fill=tk.X, expand=True)

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

