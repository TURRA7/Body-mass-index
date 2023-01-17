from os import startfile
from tkinter import *
from tkinter import messagebox


# Creating the main window.
window_1 = Tk()
window_1.title("BODY MASS INDEX")
window_1.geometry('270x100')
window_1.resizable(width=False, height=False)
lbl = Label(window_1)
lbl.grid(column=0, row=0)


# Function with text symbols.
def label(TEXT, X, Y):
    lbl = Label(window_1, text=TEXT, font=("Arial Bold", 10))
    lbl.grid(column=0, row=0)
    lbl.place(x=X, y=Y)


# The button for calculating indicators.
def button(TEXT, com, X, Y):
    btn1 = Button(window_1, text=TEXT, command=com)
    btn1.grid(column=0, row=0)
    btn1.place(x=X, y=Y)


# Mass input field.
txt1 = Entry(window_1, width=10)
txt1.grid(column=0, row=0)
txt1.place(x=80, y=10)


# Growth input field.
txt2 = Entry(window_1, width=10)
txt2.grid(column=0, row=0)
txt2.place(x=80, y=40)


# BMI calculation.
def calculate():
    weight = txt1.get()
    height = txt2.get()

    result = float(weight) / ((float(height)
                               / 100) * (float(height) / 100))
    label(int(result), 80, 70)
    if result > 18.5 and result < 25:
        messagebox.showinfo('РЕЗУЛЬТАТ', 'ВАШ ВЕС В НОРМЕ!')
    if result > 25 and result < 30:
        messagebox.showinfo('РЕЗУЛЬТАТ', 'ИЗБЫТОЧНЫЙ ВЕС!')
    if result > 30:
        messagebox.showinfo('РЕЗУЛЬТАТ', 'ОЖИРЕНИЕ!')
    if result < 18.5:
        messagebox.showinfo('РЕЗУЛЬТАТ', 'НЕДОБОР ВЕСА!')


# Message-box.
def manual():
    messagebox.showinfo('ПАМЯТКА', 'ИМТ - ИНДЕКС МАССЫ ТЕЛА.\n\
Вес указывать в формате кг.г(Килограммы.граммы).\n\
Рост указывать в СМ.')


# Calling buttons.
button('РАССЧИТАТЬ', calculate, 150, 5)
button('?', manual, 240, 5)


# Calling the notation.
label('Ваш вес:', 10, 10)
label('Ваш рост:', 10, 40)
label('Ваш ИМТ:', 10, 70)


window_1.mainloop()
