from tkinter import *

def convert():
    x = int(miles_input_value.get())
    return '{:.2f}'.format(1.60934*x)

def value():
    KM_start.config(text=convert())

window = Tk()
window.title("Miles to KM convertor")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

text1 = Label(text="Miles", font=("Arial", 12, "bold"))
text1.grid(column=0, row=0)

text2 = Label(text="KM", font=("Arial", 12, "bold"))
text2.grid(column=0, row=1)

KM_start = Label(text="0", font=("Arial", 12, "bold"))
KM_start.grid(column=1, row=1)

miles_input_value = Entry(width=10)
miles_input_value.grid(column=1, row=0)
miles_input_value.focus()

button = Button(text="convert", command=value)
button.grid(column=2, row=0)

window.mainloop()