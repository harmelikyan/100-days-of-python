from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)


#Label


my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    my_label["text"] = "I Got Clicked"


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()