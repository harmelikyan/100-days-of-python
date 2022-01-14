from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# Miles input
miles = Entry(width=10)
miles.insert(END, string=0)
miles.grid(column=1, row=0)
miles_label = Label(text="Miles", font=("Arial", 18))
miles_label.grid(column=2, row=0)

# Km output
equal_to = Label(text="is equal to", font=("Arial", 18))
equal_to.grid(column=0, row=1)

# km label
km_label = Label(text="0", font=("Arial", 18))
km_label.grid(column=1, row=1)
km_text = Label(text="Km", font=("Arial", 18))
km_text.grid(column=2, row=1)


# Calculation miles to km
def get_entry():
    km_label["text"] = round(float(miles.get()) * 1.609)


# Button to convert
button_to_convert = Button(text="Calculate", command=get_entry)
button_to_convert.grid(column=1, row=2)


window.mainloop()
