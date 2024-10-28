import tkinter as tk
from calculadora import Calculadora

class App:
    def __init__(self, root):
        self.calculadora = Calculadora()
        self.root = root
        self.root.configure(bg='black')
        self.root.title("Calculadora")
        self.root.geometry('370x370')

        #Se crea el campo de entrada de texto, se establece se coloca en la linea 0, columna 0
        #Se indica que ocuple un total de 4 columnas
        self.entrada = tk.Entry(root, width=20, font=("Comic Sans MS", 24), bg='black', fg='white', bd=0)
        self.entrada.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

        self.root.focus_force()

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('C', 1, 0), ('√', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
                         ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        for(text, row, col) in botones:
             btn = tk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.on_click(t),
                padx=20,
                pady=20,
                font=("Comic Sans MS", 18),
                bg='#1a1a1a',
                fg='white',
                relief='raised',
                highlightthickness=1,
                highlightbackground='black',
                highlightcolor='black'


            )
             btn.grid(row=row, column=col, sticky="nsew")
             btn.config(width=2, height=1)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_click(self, char):
        if char == '=':
            try:
                entrada = self.entrada.get()
                if '%' in entrada:
                    partes = entrada.split('%')
                    if len(partes) == 2:
                        base = float(partes[0])
                        porcentaje = float(partes[1])
                        result = self.calculadora.porcentaje(base, porcentaje)
                    else:
                        result = eval(entrada.replace('%', ''))
                else:
                    result = eval(entrada)
                
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(result))
            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        elif char == 'C':
            self.entrada.delete(0, tk.END)
        elif char == '√':
            try:
                valor = float(self.entrada.get())
                result = self.calculadora.raiz_cuadrada(valor)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(result))
            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        else:
            self.entrada.insert(tk.END, char)
