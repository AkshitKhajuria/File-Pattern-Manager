import tkinter as tk
#from tkinter import messagebox as mb

class Editor:
    
    def ok_button_clicked(self):
        '''Take user input for the patter parameters-
        String pattern has only one value- a single string value
        A number pattern has three parameters -start -stop -step
        Number patterns will loop from start[user ip, default=1]
        to end[user ip, def=10] with step[also user ip, def=1]'''
        
        #If it's set to string options, get the str_value
        if self.pat_type:
            self.get_num_values()
        
        #Otherwise get the num_pattern
        else:
            self.get_str_val()

    def __init__(self, widget_class):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.widget_class = widget_class
        #Some book keeping
        self.types = {0:"String", 1:"Number"} 
        #this variable tells which pattern is being currently used, string (0) or num (1)
        self.pat_type = 0 
        #Value for string pattern
        self.str_value = ""
        #Value for numeric pattern- [start, stop, step]
        self.num_pattern = [1, 10, 1] 

    def show_Editor(self, master):
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
        
        # self.Button2 = tk.Button(self.master)
        # self.Button2.place(relx=0.393, rely=0.791, height=52, width=98)
        # self.Button2.configure(activebackground="#ececec")
        # self.Button2.configure(activeforeground="#000000")
        # self.Button2.configure(background="#d9d9d9")
        # self.Button2.configure(disabledforeground="#a3a3a3")
        # self.Button2.configure(foreground="#000000")
        # self.Button2.configure(highlightbackground="#d9d9d9")
        # self.Button2.configure(highlightcolor="black")
        # self.Button2.configure(pady="0")
        # self.Button2.configure(text='''OK''')
        # self.Button2.configure(command=self.ok_button_clicked)

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
        self.Button1.configure(text=self.types[self.pat_type])
        self.Button1.configure(command=self.toggle_type)
        if self.pat_type==1:
            self.set_number_edit_options()
        else:
            self.set_string_edit_options()

    def destroy_frame(self, target:tk.Frame):
        target.destroy()

    def clear_frame(self, frame:tk.Frame):
        for child in frame.winfo_children():
            child.destroy()

    #This function toggles the type of pattern - String or Number
    def toggle_type(self):
        #If current type is String, change to Number
        if (self.pat_type == 0):
            self.pat_type = 1
            self.widget_class.set_button_text("Number")
            self.Button1.configure(text="Number")
            #Clean up the items in Configure frame
            self.clear_frame(self.Labelframe1)
            #Set up widgets for Number options
            self.set_number_edit_options()

        #Otherwise change type to String
        else:
            self.pat_type = 0
            self.widget_class.set_button_text("String")
            self.Button1.configure(text="String")
            #Clean up the items in Configure frame
            self.clear_frame(self.Labelframe1)
            #Set up widgets for String options
            self.set_string_edit_options()

    def set_string_edit_options(self):
        '''This class configures and populates the configuration options
        for string type pattern.'''
        self.seo_Label1 = tk.Label(self.Labelframe1)
        self.seo_Label1.place(relx=0.097, rely=0.345, height=41, width=137)
        self.seo_Label1.configure(background="#d9d9d9")
        self.seo_Label1.configure(disabledforeground="#a3a3a3")
        self.seo_Label1.configure(foreground="#000000")
        self.seo_Label1.configure(text='''String''')

        self.seo_Entry1 = tk.Entry(self.Labelframe1)
        self.seo_Entry1.place(relx=0.447, rely=0.345,height=36, relwidth=0.396)
        self.seo_Entry1.configure(background="white")
        self.seo_Entry1.configure(disabledforeground="#a3a3a3")
        self.seo_Entry1.configure(font="TkFixedFont")
        self.seo_Entry1.configure(foreground="#000000")
        self.seo_Entry1.configure(insertbackground="black")
        self.seo_Entry1.insert(0, self.str_value)

    def set_number_edit_options(self):
        '''This class configures and populates the configuration options
        for number type pattern.'''
        self.neo_Label2 = tk.Label(self.Labelframe1)
        self.neo_Label2.place(relx=0.058, rely=0.207, height=31, width=88)
        self.neo_Label2.configure(background="#d9d9d9")
        self.neo_Label2.configure(disabledforeground="#a3a3a3")
        self.neo_Label2.configure(foreground="#000000")
        self.neo_Label2.configure(text='''Start from''')

        self.neo_Label3 = tk.Label(self.Labelframe1)
        self.neo_Label3.place(relx=0.563, rely=0.207, height=31, width=64)
        self.neo_Label3.configure(background="#d9d9d9")
        self.neo_Label3.configure(disabledforeground="#a3a3a3")
        self.neo_Label3.configure(foreground="#000000")
        self.neo_Label3.configure(text='''Stop at''')

        self.neo_Entry2 = tk.Entry(self.Labelframe1)
        self.neo_Entry2.place(relx=0.272, rely=0.207,height=36, relwidth=0.124)
        self.neo_Entry2.configure(background="white")
        self.neo_Entry2.configure(disabledforeground="#a3a3a3")
        self.neo_Entry2.configure(font="TkFixedFont")
        self.neo_Entry2.configure(foreground="#000000")
        self.neo_Entry2.configure(insertbackground="black")
        self.neo_Entry2.insert(0, str(self.num_pattern[0]))
        
        self.neo_Entry3 = tk.Entry(self.Labelframe1)
        self.neo_Entry3.place(relx=0.738, rely=0.207,height=36, relwidth=0.124)
        self.neo_Entry3.configure(background="white")
        self.neo_Entry3.configure(disabledforeground="#a3a3a3")
        self.neo_Entry3.configure(font="TkFixedFont")
        self.neo_Entry3.configure(foreground="#000000")
        self.neo_Entry3.configure(insertbackground="black")
        self.neo_Entry3.insert(0, str(self.num_pattern[1]))

        self.neo_Label4 = tk.Label(self.Labelframe1)
        self.neo_Label4.place(relx=0.039, rely=0.621, height=31, width=67)
        self.neo_Label4.configure(background="#d9d9d9")
        self.neo_Label4.configure(disabledforeground="#a3a3a3")
        self.neo_Label4.configure(foreground="#000000")
        self.neo_Label4.configure(text='''Step''')

        self.neo_Entry4 = tk.Entry(self.Labelframe1)
        self.neo_Entry4.place(relx=0.272, rely=0.621,height=36, relwidth=0.124)
        self.neo_Entry4.configure(background="white")
        self.neo_Entry4.configure(disabledforeground="#a3a3a3")
        self.neo_Entry4.configure(font="TkFixedFont")
        self.neo_Entry4.configure(foreground="#000000")
        self.neo_Entry4.configure(insertbackground="black")
        self.neo_Entry4.insert(0, str(self.num_pattern[2]))
    
    def get_str_val(self):
        self.str_value = self.seo_Entry1.get()

    def get_num_values(self):
        '''For number patterns, get the values [start, stop, step] from entry widgets.
        Catches ValueError if non-numeric input is entered.'''
        try:
            x = int(self.neo_Entry2.get().strip())
            y = int(self.neo_Entry3.get().strip())
            z = int(self.neo_Entry4.get().strip())
        except ValueError:
            print("Please enter numeric input only.") 
            print("Number pattern set to {}".format(self.num_pattern))
        else:
            self.num_pattern[0] = x
            self.num_pattern[1] = y
            self.num_pattern[2] = z

    def get_pattern(self):
        if self.pat_type:
            t = self.num_pattern
            x = []
            for i in range(t[0], t[1]+1, t[2]):
                x.append(str(i))
            return x
        else:
            t = []
            t.append(self.str_value)
            return t
