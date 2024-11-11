import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Создаем выпадающее меню для выбора стиля
        self.style_var = tk.StringVar(value="Стандартный")
        self.style_menu = ttk.Combobox(master, textvariable=self.style_var, values=["Стандартный", "Темный", "Светлый"], state="readonly")
        self.style_menu.grid(row=0, column=4)
        self.style_menu.bind("<<ComboboxSelected>>", self.change_style)

        # Поле ввода
        self.result_display = tk.Entry(master, textvariable=self.result_var, font=("Arial", 30), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_display.grid(row=1, column=0, columnspan=4)

        self.create_buttons()
        self.apply_style()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 2
        col = 0
        for button in buttons:
            btn = tk.Button(self.master, text=button, padx=40, pady=20, font=("Arial", 20), command=lambda b=button: self.append_to_expression(b))
            btn.grid(row=row, column=col)
            if button == '=':
                btn.config(command=self.calculate)
            elif button == 'C':
                btn.config(command=self.clear)
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

    def apply_style(self):
        style = self.style_var.get()
        if style == "Стандартный":
            self.master.config(bg="lightgray")
            self.result_display.config(bg="white", fg="black")
        elif style == "Темный":
            self.master.config(bg="black")
            self.result_display.config(bg="darkgray", fg="white")
        elif style == "Светлый":
            self.master.config(bg="white")
            self.result_display.config(bg="lightyellow", fg="black")

        # Обновляем стиль кнопок
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                if style == "Стандартный":
                    widget.config(bg="lightblue", fg="black")
                elif style == "Темный":
                    widget.config(bg="gray", fg="white")
                elif style == "Светлый":
                    widget.config(bg="lightgreen", fg="black")

    def change_style(self, event):
        self.apply_style()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

