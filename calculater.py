from tkinter import *

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def evaluate_expression():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear_expression():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.title("Simple Calculator")
    gui.geometry("300x80")
    gui.configure(background="light green")

    expression = ""
    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('Arial', 20), bd=5, insertwidth=2, width=10, justify='right', bg='black', fg='white')
    expression_field.grid(row=0, column=0, columnspan=4)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
    ]

    for (text, row, col) in buttons:
        button = Button(gui, text=text, fg='white', bg='black', font=('Arial', 14, 'bold'), height=2, width=8)
        if text == "=":
            button.config(command=evaluate_expression)
        elif text == "C":
            button.config(command=clear_expression)
        else:
            button.config(command=lambda t=text: press(t))
        button.grid(row=row, column=col)

    gui.mainloop()
