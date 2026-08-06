from tkinter import *
from tkinter import font

window = Tk()
window.title("mile to km converter app")
window.minsize(500, 300)

def convert_to_km():
    value_in_miles = float(input.get())
    converted_label["text"] = value_in_miles * 1.60934

input = Entry()
input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(row=0, column=12)

equal_label = Label(text="Equals to", font=("Arial", 20, "normal"))
equal_label.grid(row=1, column=0)

converted_label = Label(text="?", font=("Arial", 20, "normal"))
converted_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=convert_to_km, font=("Arial", 20, "normal"))
calculate_button.grid(row=2, column=1)

window.mainloop()