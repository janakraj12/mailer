import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x500")
        self.result_var = tk.StringVar()

        self.create_widgets()
    
    def create_widgets(self):
        entry = tk.Entry(self, textvar=self.result_var, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, justify='right')
        entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'acos',
            '0', '.', '=', '+', 'asin'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=("Helvetica", 20), bd=8, command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_expression = self.result_var.get()
        if button == "=":
            try:
                result = eval(current_expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button == "sqrt":
            try:
                result = math.sqrt(float(current_expression))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_expression + button)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
