from tkinter import *
from tkinter import ttk

class MyApp(ttk.Frame):
    
    def __init__(self, master=None):
        
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        
        self.entry_var = StringVar(value='0')
        self.entry = ttk.Entry(self, textvariable=self.entry_var, justify='right')
        self.entry.grid(row=0, column=0, columnspan= 4, sticky='EW', padx=5, pady=5)
        
        self.percent = ttk.Button(self, text = '%', command= None)
        self.percent.grid(row=1, column=0, padx=2, pady=2)
        
        self.clear_digit = ttk.Button(self, text = 'CE', command=None)
        self.clear_digit.grid(row=1, column = 1, padx=2, pady=2)
        
        self.clear_all= ttk.Button(self, text = 'C', command=None)
        self.clear_all.grid(row=1, column = 2, padx=2, pady=2)
        
        self.deletebtn = ttk.Button(self, text = 'DEL', command=None)
        self.deletebtn.grid(row=1, column = 3, padx=2, pady=2)
        
        self.homofunc = ttk.Button(self, text = '1/x', command= None)
        self.homofunc.grid(row=2, column=0, padx=2, pady=2)
        
        self.squarre = ttk.Button(self, text = 'x^2', command=None)
        self.squarre.grid(row=2, column = 1, padx=2, pady=2)
        
        self.squarre_root= ttk.Button(self, text = 'x^(1/2)', command=None)
        self.squarre_root.grid(row=2, column = 2, padx=2, pady=2)
        
        self.division = ttk.Button(self, text = '/', command=None)
        self.division.grid(row=2, column = 3, padx=2, pady=2)
        
        self.digits = [ttk.Button(self, text = str(i), command=None) for i in range(9,0,1)]
        for i, widget in enumerate(self.digits):
            widget.grid(x=3+(i//3) , y=3 , padx=2, pady=2)

root = Tk()
root.title('Caculator')
myapp = MyApp(root)
myapp.mainloop()
    
    