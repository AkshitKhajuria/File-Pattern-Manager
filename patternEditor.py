import tkinter as tk

class Editor:
    def __init__(self, master, widget_class):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.widget_class = widget_class
        self.master = master

        self.master.geometry("484x354+650+150")
        self.master.minsize(176, 1)
        self.master.maxsize(1924, 1050)
        self.master.resizable(1, 1)
        self.master.title("Pattern Editor")
        self.master.configure(background="#d9d9d9")

        self.Labelframe1 = tk.LabelFrame(self.master)
        self.Labelframe1.place(relx=0.124, rely=0.367, relheight=0.342
                , relwidth=0.75)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Configure''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.Button2 = tk.Button(self.master)
        self.Button2.place(relx=0.393, rely=0.791, height=52, width=98)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')

        self.Labelframe2 = tk.LabelFrame(self.master)
        self.Labelframe2.place(relx=0.289, rely=0.056, relheight=0.268
                , relwidth=0.393)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Type''')
        self.Labelframe2.configure(background="#d9d9d9")

        self.Button1 = tk.Button(self.Labelframe2)
        self.Button1.place(relx=0.105, rely=0.316, height=52, width=148
                , bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text=self.widget_class.types[self.widget_class.pat_type])
        self.Button1.configure(command=self.toggle_type)

    def toggle_type(self):
        current_type = self.widget_class.pat_type
        if (current_type == 0):
            self.widget_class.set_type(1)
            self.Button1.configure(text="Number")
        else:
            self.widget_class.set_type(0)
            self.Button1.configure(text="String")
        
