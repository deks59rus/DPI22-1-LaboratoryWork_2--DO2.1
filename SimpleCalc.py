import tkinter as tk
from tkinter import ttk, messagebox
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        # Добавление названия для калькулятора
        self.title_label = ttk.Label(master, text="Калькулятор", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.result_var = tk.StringVar()
        self.result_var.set("")
        self.history = []  # Список для хранения истории вычислений

        # Создаем выпадающее меню для выбора стиля
        self.style_var = tk.StringVar(value="Стандартный")
        self.style_menu = ttk.Combobox(master, textvariable=self.style_var, values=["Стандартный", "Темный", "Светлый"],
                                       state="readonly")
        self.style_menu.grid(row=0, column=5, padx=10, pady=10)
        self.style_menu.bind("<<ComboboxSelected>>", self.change_style)

        # Поле ввода
        self.result_display = ttk.Entry(master, textvariable=self.result_var, font=("Arial", 30), justify='right')
        self.result_display.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        self.result_display.bind("<Return>", self.calculate)  # Обработка нажатия Enter

        self.create_buttons()
        self.apply_style()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', '^',
            '0', '=', '+', '%', '←',
            '(', ')', 'sin', 'cos', 'tan', 'log', 'history'
        ]

        row = 2
        col = 0
        for button in buttons:
            btn = ttk.Button(self.master, text=button, command=lambda b=button: self.append_to_expression(b))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if button == '=':
                btn.config(command=self.calculate)
            elif button == 'C':
                btn.config(command=self.clear)
            elif button == '←':
                btn.config(command=self.undo)
            elif button == 'history':
                btn.config(command=self.show_history)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def append_to_expression(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def calculate(self, event=None):  # Добавлен параметр event
        expression = self.result_var.get()
        try:
            # Обработка новых операций
            expression = expression.replace('^', '**')  # Возведение в степень
            expression = expression.replace('√', 'math.sqrt')  # Квадратный корень
            expression = expression.replace('%', '/100')  # Процент
            expression = expression.replace('sin', 'math.sin')  # Синус
            expression = expression.replace('cos', 'math.cos')  # Косинус
            expression = expression.replace('tan', 'math.tan')  # Тангенс
            expression = expression.replace('log', 'math.log10')  # Логарифм по основанию 10

            result = eval(expression)
            self.result_var.set(result)
            self.history.append(f"{expression} = {result}")  # Сохраняем в историю
        except Exception as e:
            self.result_var.set("Ошибка")
            print(e)

    def clear(self):
        self.result_var.set("")

    def undo(self):
        if self.history:
            last_operation = self.history.pop()  # Удаляем последний элемент из истории
            self.result_var.set(last_operation.split('=')[0].strip())  # Возвращаем выражение
        else:
            self.result_var.set("")

    def show_history(self):
        if not self.history:
            messagebox.showinfo("История", "История пуста.")
        else:
            history_str = "\n".join(self.history)
            messagebox.showinfo("История", history_str)

    def apply_style(self):
        style = self.style_var.get()
        if style == "Стандартный":
            self.master.config(bg="lightgray")
            self.result_display.config(style='TEntry')
            ttk.Style().configure('TButton', background='lightblue', foreground='black')
        elif style == "Темный":
            self.master.config(bg="black")
            self.result_display.config(style='TEntry')
            ttk.Style().configure('TButton', background='gray', foreground='black')
        elif style == "Светлый":
            self.master.config(bg="white")
            self.result_display.config(style='TEntry')
            ttk.Style().configure('TButton', background='lightgreen', foreground='black')

        # Обновляем стиль кнопок
        for widget in self.master.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.config(style='TButton')

    def change_style(self, event):
        self.apply_style()


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
