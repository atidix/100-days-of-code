import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometres Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def convert():
    miles = float(input.get())
    km = round(miles * 1.60, 2)
    kms_label.config(text=km)

input = tkinter.Entry(width=5)
input.insert(tkinter.END, string="0")
input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 15))
miles_label.grid(row=0, column=2, padx=10)

is_equal_to_label = tkinter.Label(text="is equal to", font=("Arial", 15))
is_equal_to_label.grid(row=1, column=0)

kms_label = tkinter.Label(text=0, font=("Arial", 15))
kms_label.grid(row=1, column=1)

kilometres_label = tkinter.Label(text="Kilometres", font=("Arial", 15))
kilometres_label.grid(row=1, column=2)

calculate = tkinter.Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)


window.mainloop()