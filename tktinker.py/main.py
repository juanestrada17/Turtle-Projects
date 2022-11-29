from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="New text", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Entry

input = Entry(width=10)
input.grid(column=2, row=2)


# Button

def button_clicked():
    return my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Button 2
button2 = Button(text="No, Click me!")
button2.grid(column=2, row=0)

window.mainloop()


