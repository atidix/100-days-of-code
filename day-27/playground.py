import tkinter

def button_click():
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text= "New text")
my_label.grid(row=0, column=0)

button = tkinter.Button(text="click me", command=button_click)
button.grid(row=1, column=1)

new_button= tkinter.Button(text="new button")
new_button.grid(row=0, column=2)

input = tkinter.Entry(width=10)
input.grid(row=3, column=3)

window.mainloop()