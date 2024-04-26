import tkinter as tk
from tkinter import *
from read_database import calculation

def window(event=None):
    div_list = calculation(num.get())
    root.destroy()
    root2 = tk.Tk()
    root2.title("Calculation")
    root2.geometry('350x400')
    d = Text(root2)
    for x in div_list:
        d.insert(END, str(x) + '\n')
    d.pack()

root = tk.Tk()
root.title("Dividend Calculation")
root.geometry('350x200')

label = tk.Label(root, text="Dividend Calculator")
label.grid(row=1, column=1, columnspan=2, pady=0, padx= 115)    

label = tk.Label(root, text="Input ID: ")
label.grid(row=2, column=1, columnspan=1, pady=0, padx= 0)   

num = tk.Entry(root)
num.grid(row = 3, column = 1, pady=0, padx=115)

root.bind('<Return>', window)

button = tk.Button(root, text="Calculate", command=window)
button.grid(row=4, column=1 , columnspan=2)

root.mainloop()