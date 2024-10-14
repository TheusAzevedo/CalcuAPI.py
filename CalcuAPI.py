import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Calculator')
        self.window.resizable(width=False, height=False)

        self.result = ""
        self.WIDTH = 10
        self.HEIGHT = 3
        self.font = 'Arial 14 bold'
        
        self.result_display = tk.Label(self.window)
        
        self.auxResult = tk.StringVar()
        self.auxResult.set('0')
        self.lbResult = tk.Label(self.window, textvariable=self.auxResult, font=self.font)
        self.lbResult.grid(row=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.window, text=button, width=self.WIDTH, height=self.HEIGHT, font=self.font, command=lambda value=button: self.update(value)).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.window.mainloop()

    def update(self, value):
        if value == 'C':
            self.result = ""
        elif value == '=':
            self.calculate()
        else:
            self.result += value
        self.auxResult.set(self.result)

    def calculate(self):
        try:
            result = eval(self.result)
            self.result = str(result)
        except:
            self.result = "Unable to calculate"
        self.auxResult.set(self.result)

Calculator()
