import tkinter as tk

class Calculadora:
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title('Calculadora')
        self.tela.resizable(width=False, height=False)

        self.result = ""
        self.WIDTH = 10
        self.HEIGHT = 3
        self.fonte = 'Arial 14 bold'
        
        self.resultado = tk.Label(self.tela)
        
        self.auxResultado = tk.StringVar()
        self.auxResultado.set('0')
        self.lbResultado = tk.Label(self.tela, textvariable=self.auxResultado, font=self.fonte)
        self.lbResultado.grid(row=0, columnspan=4, pady=10)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for botao in botoes:
            tk.Button(self.tela, text=botao, width=self.WIDTH, height=self.HEIGHT, font=self.fonte, command=lambda valor=botao: self.atualizar(valor)).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.tela.mainloop()

    def atualizar(self, valor):
        if valor == 'C':
            self.result = ""
        elif valor == '=':
            self.calcular()
        else:
            self.result += valor
        self.auxResultado.set(self.result)

    def calcular(self):
        try:
            resultado = eval(self.result)
            self.result = str(resultado)
        except:
            self.result = "Impossivel calcular"
        self.auxResultado.set(self.result)

Calculadora()