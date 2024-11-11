import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Увеличиваем размер шрифта в поле ввода
        self.result_display = tk.Entry(master, textvariable=self.result_var, font=("Arial", 30), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            # Увеличиваем размер шрифта на кнопках
            tk.Button(self.master, text=button, padx=40, pady=20, font=("Arial", 20), command=lambda b=button: self.append_to_expression(b)).grid(row=row, column=col)
            if button == '=':
                tk.Button(self.master, text=button, padx=40, pady=20, font=("Arial", 20), command=self.calculate).grid(row=row, column=col)
            elif button == 'C':
                tk.Button(self.master, text=button, padx=40, pady=20, font=("Arial", 20), command=self.clear).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def append_to_expression(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Ошибка")

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
