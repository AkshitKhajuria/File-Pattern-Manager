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

        t = self.widget_class.pat_type
        if t==0:
            self.x=string_edit_options(self.Labelframe1)
        else:
            self.x=number_edit_options(self.Labelframe1)
        
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

    def destroy_frame(self, target:tk.Frame):
        target.destroy()

    #This function toggles the type of pattern - String or Number
    def toggle_type(self):
        current_type = self.widget_class.pat_type
        #If current type is String, change to Number
        if (current_type == 0):
            self.widget_class.set_type(1)
            self.Button1.configure(text="Number")
            #Clean up the items in Configure frame
            self.x.destroy_frame()
            del self.x
            #Set up widgets for Number options
            self.x = number_edit_options(self.Labelframe1)

        #Otherwise change type to String
        else:
            self.widget_class.set_type(0)
            self.Button1.configure(text="String")
            #Clean up the items in Configure frame
            self.x.destroy_frame()
            del self.x
            #Set up widgets for String options
            self.x = string_edit_options(self.Labelframe1)


class string_edit_options(Editor):
    def __init__(self, top):
        '''This class configures and populates the configuration options
        for string type pattern.'''
        self.seo_Frame1 = tk.Frame(top)
        self.seo_Frame1.pack(fill=tk.BOTH, expand=True)
        #self.seo_Frame1.configure(relief='groove')
        self.seo_Frame1.configure(borderwidth="2")
        self.seo_Frame1.configure(relief="groove")
        self.seo_Frame1.configure(background="#d9d9d9")

        self.seo_Label1 = tk.Label(self.seo_Frame1)
        self.seo_Label1.place(relx=0.097, rely=0.345, height=41, width=137)
        self.seo_Label1.configure(background="#d9d9d9")
        self.seo_Label1.configure(disabledforeground="#a3a3a3")
        self.seo_Label1.configure(foreground="#000000")
        self.seo_Label1.configure(text='''String''')

        self.seo_Entry1 = tk.Entry(self.seo_Frame1)
        self.seo_Entry1.place(relx=0.447, rely=0.345,height=36, relwidth=0.396)
        self.seo_Entry1.configure(background="white")
        self.seo_Entry1.configure(disabledforeground="#a3a3a3")
        self.seo_Entry1.configure(font="TkFixedFont")
        self.seo_Entry1.configure(foreground="#000000")
        self.seo_Entry1.configure(insertbackground="black")
    
    def destroy_frame(self):
        self.seo_Frame1.destroy()

class number_edit_options(Editor):
    def __init__(self, top):
        '''This class configures and populates the configuration options
        for number type pattern.'''
        self.neo_Frame2 = tk.Frame(top)
        self.neo_Frame2.pack(fill=tk.BOTH, expand=True)
        #self.neo_Frame2.configure(relief='groove')
        self.neo_Frame2.configure(borderwidth="2")
        self.neo_Frame2.configure(relief="groove")
        self.neo_Frame2.configure(background="#d9d9d9")

        self.neo_Label2 = tk.Label(self.neo_Frame2)
        self.neo_Label2.place(relx=0.058, rely=0.207, height=31, width=88)
        self.neo_Label2.configure(background="#d9d9d9")
        self.neo_Label2.configure(disabledforeground="#a3a3a3")
        self.neo_Label2.configure(foreground="#000000")
        self.neo_Label2.configure(text='''Start from''')

        self.neo_Label3 = tk.Label(self.neo_Frame2)
        self.neo_Label3.place(relx=0.563, rely=0.207, height=31, width=64)
        self.neo_Label3.configure(background="#d9d9d9")
        self.neo_Label3.configure(disabledforeground="#a3a3a3")
        self.neo_Label3.configure(foreground="#000000")
        self.neo_Label3.configure(text='''Stop at''')

        self.neo_Entry2 = tk.Entry(self.neo_Frame2)
        self.neo_Entry2.place(relx=0.272, rely=0.207,height=36, relwidth=0.124)
        self.neo_Entry2.configure(background="white")
        self.neo_Entry2.configure(disabledforeground="#a3a3a3")
        self.neo_Entry2.configure(font="TkFixedFont")
        self.neo_Entry2.configure(foreground="#000000")
        self.neo_Entry2.configure(insertbackground="black")

        self.neo_Entry3 = tk.Entry(self.neo_Frame2)
        self.neo_Entry3.place(relx=0.738, rely=0.207,height=36, relwidth=0.124)
        self.neo_Entry3.configure(background="white")
        self.neo_Entry3.configure(disabledforeground="#a3a3a3")
        self.neo_Entry3.configure(font="TkFixedFont")
        self.neo_Entry3.configure(foreground="#000000")
        self.neo_Entry3.configure(insertbackground="black")

        self.neo_Label4 = tk.Label(self.neo_Frame2)
        self.neo_Label4.place(relx=0.039, rely=0.621, height=31, width=67)
        self.neo_Label4.configure(background="#d9d9d9")
        self.neo_Label4.configure(disabledforeground="#a3a3a3")
        self.neo_Label4.configure(foreground="#000000")
        self.neo_Label4.configure(text='''Step''')

        self.neo_Entry4 = tk.Entry(self.neo_Frame2)
        self.neo_Entry4.place(relx=0.272, rely=0.621,height=36, relwidth=0.124)
        self.neo_Entry4.configure(background="white")
        self.neo_Entry4.configure(disabledforeground="#a3a3a3")
        self.neo_Entry4.configure(font="TkFixedFont")
        self.neo_Entry4.configure(foreground="#000000")
        self.neo_Entry4.configure(insertbackground="black")

    def destroy_frame(self):
        self.neo_Frame2.destroy()

