from tkinter import *
from tkinter import ttk

class MyApp(ttk.Frame):
    
    def __init__(self, master=None):
        
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        #Dodanie głównego pola wprowadzania
        self.entry_var = StringVar(value='0')
        self.entry = ttk.Entry(self, textvariable=self.entry_var, justify='right')
        self.entry.grid(row=0, column=0, columnspan= 4, sticky='EW', padx=5, pady=5)
        #Dodanie przycisku procent
        self.percent = ttk.Button(self, text = '%', command= None)
        self.percent.grid(row=1, column=0, padx=2, pady=2)
        #Dodanie przycisku CE
        self.clear_digit = ttk.Button(self, text = 'CE', command=None)
        self.clear_digit.grid(row=1, column = 1, padx=2, pady=2)
        #Dodanie przycisku C
        self.clear_all= ttk.Button(self, text = 'C', command=None)
        self.clear_all.grid(row=1, column = 2, padx=2, pady=2)
        #Dodanie przycisku backspace
        self.deletebtn = ttk.Button(self, text = 'DEL', command=None)
        self.deletebtn.grid(row=1, column = 3, padx=2, pady=2)
        #Dodanie przycisku funkcji 1/x
        self.homofunc = ttk.Button(self, text = '1/x', command= None)
        self.homofunc.grid(row=2, column=0, padx=2, pady=2)
        #Dodanie przycisku kwadratu liczby
        self.squarre = ttk.Button(self, text = 'x^2', command=None)
        self.squarre.grid(row=2, column = 1, padx=2, pady=2)
        #Dodanie przycisku pierwiastka z liczby
        self.squarre_root= ttk.Button(self, text = 'x^(1/2)', command=None)
        self.squarre_root.grid(row=2, column = 2, padx=2, pady=2)
        #Dodanie przycisku działania dzielenia
        self.division = ttk.Button(self, text = '/', command=None)
        self.division.grid(row=2, column = 3, padx=2, pady=2)
        #Dodanie przycisków numerycznych bez zera
        self.digits = [ttk.Button(self, text = str(i), command=None) for i in range(9,0,-1)]
        for i, widget in enumerate(self.digits):
            widget.grid(row=3+(i//3) , column=i%3 , padx=2, pady=2)
        #Dodanie do self.digits przysicku zera i umieszczenie
        self.digits.append(ttk.Button(self, text = '0', command=None))
        self.digits[-1].grid(row=6, column=1, padx=2, pady=2)
        #Dodanie przycisku mnożenia
        self.multiply = ttk.Button(self, text = '*', command=None)
        self.multiply.grid(row=3, column=3, padx=2, pady=2)
        #Dodanie przycisku odejmowania
        self.substact = ttk.Button(self, text = '-', command=None)
        self.substact.grid(row=4, column=3, padx=2, pady=2)
        #Dodanie przycisku dodawania
        self.adding = ttk.Button(self, text = '+', command=None)
        self.adding.grid(row=5, column=3, padx=2, pady=2)
        # Dodanie przycisku znaku liczby
        self.signing = ttk.Button(self, text = '+/-', command=None)
        self.signing.grid(row=6, column=0, padx=2, pady=2)
        #Dodanie przysicku kropki dziesiętnej
        self.dot_float = ttk.Button(self, text = '.', command=None)
        self.dot_float.grid(row=6, column=2, padx=2, pady=2)
        #Dodanie przysicku równa się
        self.make_equal = ttk.Button(self, text = '=', command=None)
        self.make_equal.grid(row=6, column=3, padx=2, pady=2)
root = Tk()
root.title('Caculator')
myapp = MyApp(root)
myapp.mainloop()
    
    