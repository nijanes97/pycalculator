from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

num1 = 0
operator = ''

def button_add(number):
    global operator
    if operator == '=':
        e.delete(0, END)
        operator = ''
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + number)

def button_clr():
    e.delete(0, END)

def button_math(oprtr):
    global num1
    global operator
    num1 = float(e.get())
    operator = oprtr
    e.delete(0, END)

def button_equals():
    global num1
    global operator
    if operator == '+':
        num1 += float(e.get())
        if num1 % 1 == 0:
            num1 = int(num1)
        e.delete(0, END)
        e.insert(0, num1)
        num1 = 0
        operator = '='
    if operator == '-':
        num1 -= float(e.get())
        if num1 % 1 == 0:
            num1 = int(num1)
        e.delete(0, END)
        e.insert(0, num1)
        num1 = 0
        operator = '='
    if operator == '/':
        num1 /= float(e.get())
        if num1 % 1 == 0:
            num1 = int(num1)
        e.delete(0, END)
        e.insert(0, num1)
        num1 = 0
        operator = '='
    if operator == '*':
        num1 *= float(e.get())
        if num1 % 1 == 0:
            num1 = int(num1)
        e.delete(0, END)
        e.insert(0, num1)
        num1 = 0
        operator = '='


# define buttons

button_1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: button_add('1'))
button_2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: button_add('2'))
button_3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: button_add('3'))
button_4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: button_add('4'))
button_5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: button_add('5'))
button_6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: button_add('6'))
button_7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: button_add('7'))
button_8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: button_add('8'))
button_9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: button_add('9'))
button_0 = Button(root, text = '0', padx = 80, pady = 20, command = lambda: button_add('0'))

button_plus = Button(root, text = '+', padx = 40, pady = 52, command = lambda: button_math('+'))
button_minus = Button(root, text = '-', padx = 40, pady = 20, command = lambda: button_math('-'))
button_divide = Button(root, text = '/', padx = 40, pady = 20, command = lambda: button_math('/'))
button_multiply = Button(root, text = '*', padx = 40, pady = 20, command = lambda: button_math('*'))
button_equal = Button(root, text = '=', padx = 40, pady = 52, command = button_equals)

button_decimal = Button(root, text = '.', padx = 40, pady = 20, command = lambda: button_add('.'))

button_clear = Button(root, text = 'C', padx = 40, pady = 20, command = lambda: button_clr())

# put buttons on the screen

button_clear.grid(row = 1, column = 0)
button_divide.grid(row = 1, column = 1)
button_multiply.grid(row = 1, column = 2)
button_minus.grid(row = 1, column = 3)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)

button_plus.grid(row = 2, column = 3, rowspan = 2)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_equal.grid(row = 4, column = 3, rowspan = 2)

button_0.grid(row = 5, column = 0, columnspan = 2)
button_decimal.grid(row = 5, column = 2)


root.mainloop()