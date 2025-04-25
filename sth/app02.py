from tkinter import *
from tkinter import ttk
import operator

class MyApp(ttk.Frame):
    
    def __init__(self, master=None):
        '''Konstruktor głównego okna '''
        super().__init__(master)
        self.master = master
        self.grid()
        # Inicjalizacja kontenera
        self.numbers = []
        self.create_widgets()
        #Inicjalizacja zmiennej która przechowuje operacje na zmiennych w kontenerze
        self.operation = None
        
        #flaga do resetowania wartości w entry_var dla lepszego efektu
        self.reset_entry_flag = False
    
    def clear_all(self):
        '''Czyszczenie rejestru kalkulatora.'''
        self.numbers = []
        self.entry_var.set(value= '0')

    def numbers_append(self, math_operation = None):
        '''Dodanie wartości do kontenera po naciśnięciu klawiszy działania'''
        if math_operation != None:
            self.operation = math_operation
        detect_type = lambda x: float(x) if '.' in self.entry_var.get() else int(x)
        self.numbers.append(detect_type(self.entry_var.get()))
        #self.entry_var.set('0')
        self.reset_entry_flag = True
        self.temp_var.set(', '.join(map(str, self.numbers)))
    
    def insert_digit(self, digit):
        ''' Metoda wstawienia cyfry do głównej etykiety 'entry'.'''
        if self.entry_var.get() == '0' or self.reset_entry_flag:
            self.entry_var.set(value='')
            self.reset_entry_flag = False
        self.entry_var.set(value=self.entry_var.get() + digit)  
    
    def clear_last_digit(self):
        ''' Usunięcie ostatniej cyfry z etykiety 'entry'.'''
        self.entry_var.set(value=self.entry_var.get()[:-1])
        if self.entry_var.get() == '':
            self.entry_var.set(value= '0')
    
    def count(self):
        '''Metoda liczenia elementów kontenera - naciśnięcie przycisku '=' lub kolejnej operacji 'self.operation'.'''
        if not self.entry_var.get() == '':
            self.numbers_append()
        if len(self.numbers) == 1:
            self.entry_var.set(str(self.numbers[0]))
        elif len(self.numbers) > 1:
            try:
                result = self.operation(self.numbers[-2], self.numbers[-1])
            except ZeroDivisionError:
                self.entry_var.set('Dzielenie przez zero!!!')
            else:
                self.numbers.clear() 
                self.numbers.append(result)
                self.entry_var.set(str(self.numbers[-1]))
        
    def insert_dot(self):
        '''Metoda wstawienia kropki(separatora dziesiętnego) do etykiety 'entry'.'''
        if self.entry_var.get() == '0' or (not '.' in self.entry_var.get()):
            self.entry_var.set(value=self.entry_var.get() + '.') 
    
    def create_widgets(self):
        '''Tworzenie okna z widgetami.'''
        #Dodanie głównego pola wprowadzania
        self.entry_var = StringVar(value='0')
        #self.entry = ttk.Entry(self, textvariable=self.entry_var, justify='right')
        self.entry = ttk.Label(self, anchor= 'e', background='white', foreground='black', textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, columnspan= 4, sticky='EW', padx=5, pady=5)
        #Dodanie przycisku procent
        self.percent = ttk.Button(self, text = '%', command= None)
        self.percent.grid(row=1, column=0, padx=2, pady=2)
        #Dodanie przycisku CE
        self.clear_digit = ttk.Button(self, text = 'CE', command=None)
        self.clear_digit.grid(row=1, column = 1, padx=2, pady=2)
        #Dodanie przycisku C
        self.clear_all= ttk.Button(self, text = 'C', command=self.clear_all)
        self.clear_all.grid(row=1, column = 2, padx=2, pady=2)
        #Dodanie przycisku backspace
        self.deletebtn = ttk.Button(self, text = 'DEL', command=self.clear_last_digit)
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
        self.division = ttk.Button(self, text = '/', command=lambda: self.numbers_append(operator.truediv))
        self.division.grid(row=2, column = 3, padx=2, pady=2)
        #Dodanie przycisków numerycznych bez zera
        self.digits = [ttk.Button(self, text = str(i), command=lambda digit = str(i): self.insert_digit(digit)) for i in range(9,0,-1)]
        for i, widget in enumerate(self.digits):
            widget.grid(row=3+(i//3) , column=i%3 , padx=2, pady=2)
        #Dodanie do self.digits przysicku zera i umieszczenie
        self.digits.append(ttk.Button(self, text = '0', command=lambda: self.insert_digit('0')))
        self.digits[-1].grid(row=6, column=1, padx=2, pady=2)
        #Dodanie przycisku mnożenia
        self.multiply = ttk.Button(self, text = '*', command=lambda: self.numbers_append(operator.mul))
        self.multiply.grid(row=3, column=3, padx=2, pady=2)
        #Dodanie przycisku odejmowania
        self.substact = ttk.Button(self, text = '-', command=lambda: self.numbers_append(operator.sub))
        self.substact.grid(row=4, column=3, padx=2, pady=2)
        #Dodanie przycisku dodawania
        self.adding = ttk.Button(self, text = '+', command=lambda: self.numbers_append(operator.add))
        self.adding.grid(row=5, column=3, padx=2, pady=2)
        # Dodanie przycisku znaku liczby
        self.signing = ttk.Button(self, text = '+/-', command=None)
        self.signing.grid(row=6, column=0, padx=2, pady=2)
        #Dodanie przysicku kropki dziesiętnej
        self.dot_float = ttk.Button(self, text = '.', command=self.insert_dot)
        self.dot_float.grid(row=6, column=2, padx=2, pady=2)
        #Dodanie przysicku równa się
        self.make_equal = ttk.Button(self, text = '=', command=self.count)
        self.make_equal.grid(row=6, column=3, padx=2, pady=2)
        
        #etykieta tymczasowa
        self.temp_var = StringVar()
        self.temp= ttk.Label(self, anchor= 'center', background='white', foreground='black', textvariable=self.temp_var)
        self.temp.grid(row=7, column=0, columnspan= 4, sticky='EW', padx=5, pady=5)
        
root = Tk()
root.title('Caculator')
root.resizable(False, False)
myapp = MyApp(root)
myapp.mainloop()
    
    