from tkinter import *

def button_clicked():
    print("clicked")
    new_text = input.get()
    my_label.config(text= new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


my_label = Label(window, text="My first GUI Program" , font=("Arial",24,"bold"))
my_label.config(text= "New text")
my_label.grid(row=0, column=0)


button = Button(text="Click Me" , command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="new button")
new_button.grid(row=0, column=2)

input = Entry(width=40)
print(input.get())
input.grid(row=3, column=2)



window.mainloop()