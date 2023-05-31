import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.display = tk.Entry(master, width=40, borderwidth=70)
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=40)

        button_1 = self.create_button("1", 1, 0)
        button_2 = self.create_button("2", 1, 1)
        button_3 = self.create_button("3", 1, 2)
        button_4 = self.create_button("4", 2, 0)
        button_5 = self.create_button("5", 2, 1)
        button_6 = self.create_button("6", 2, 2)
        button_7 = self.create_button("7", 3, 0)
        button_8 = self.create_button("8", 3, 1)
        button_9 = self.create_button("9", 3, 2)
        button_0 = self.create_button("0", 4, 1)

        button_add = self.create_button("+", 1, 3)
        button_subtract = self.create_button("-", 2, 3)
        button_multiply = self.create_button("*", 3, 3)
        button_divide = self.create_button("/", 4, 3)
        button_equal = self.create_button("=", 4, 2)
        button_clear = self.create_button("C", 4, 0)

        self.first_num = None
        self.operation = None
        self.is_new_num = True

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=40, pady=20, command=lambda button_text=text: self.button_click(button_text))
        button.grid(row=row, column=column)
        return button

    def button_click(self, button_text):
        current = self.display.get()

        if button_text == "C":
            self.display.delete(0, tk.END)
            self.first_num = None
            self.operation = None
            self.is_new_num = True
        elif button_text in "+-*/":
            if current != '':
                self.first_num = float(current)
                self.operation = button_text
                self.is_new_num = True
        elif button_text == "=":
            if self.first_num is not None and self.operation is not None and current != "":
                second_num = float(current)
                if self.operation == "+":
                    result = self.first_num + second_num
                elif self.operation == "-":
                    result = self.first_num - second_num
                elif self.operation == "*":
                    result = self.first_num * second_num
                elif self.operation == "/":
                    result = self.first_num / second_num
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.is_new_num = True
        else:
            if self.is_new_num:
                self.display.delete(0, tk.END)
                self.is_new_num = False
            self.display.insert(tk.END, button_text)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
