from tkinter import * # type: ignore
import tkinter as tk
from call import start


def window(event=None):
    div = start(identifier.get())
    root.destroy()
    root2 = tk.Tk()
    root2.title("Calculation")
    root2.geometry('350x400')
    d = Text(root2)
    for i in div:
        d.insert(END, i + '\n')
    d.pack()

root = tk.Tk()
root.title("Dividend Calculation")
root.geometry('300x200')

label = tk.Label(root, text="Dividend Calculator")
label.grid(row=1, column=2, columnspan=2, pady=0, padx= 0)    

label = tk.Label(root, text="Input StockID: ")
label.grid(row=2, column=1, columnspan=1, pady=0, padx= 0)   

identifier = tk.Entry(root)
identifier .grid(row = 2, column = 2, pady=0, padx=0)

root.bind('<Return>', window)

button = tk.Button(root, text="Calculate", command=window)
button.grid(row=4, column=2 , columnspan=2)

root.mainloop()