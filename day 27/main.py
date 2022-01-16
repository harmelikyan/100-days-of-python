from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    my_label["text"] = input.get()


input = Entry()
input.grid(column=3, row=2)


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)


window.mainloop()