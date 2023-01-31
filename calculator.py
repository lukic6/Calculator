from tkinter import *
from tkinter import ttk
import tkinter as tk
root = Tk()
root.geometry("300x275")

result = tk.Text(root, height= 2, width = 16, font=("Comic Sans", 24))
result.grid(columnspan=5)



calculation = ""
def write(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def clear():
    global calculation
    calculation = ""
    result.delete(1.0, "end")

def calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
    except:
        clear()
        result.insert(1.0, "Error")



ttk.Button(root, text="C", command=lambda: clear()).grid(column=1, row=5)
ttk.Button(root, text="(", command=lambda: write("(")).grid(column=1, row=9)
ttk.Button(root, text=")", command=lambda: write(")")).grid(column=3, row=9)
ttk.Button(root, text=":", command=lambda: write("/")).grid(column=4, row=5)
ttk.Button(root, text="7", command=lambda: write(7)).grid(column=1, row=6)
ttk.Button(root, text="8", command=lambda: write(8)).grid(column=2, row=6)
ttk.Button(root, text="9", command=lambda: write(9)).grid(column=3, row=6)
ttk.Button(root, text="X", command=lambda: write("*")).grid(column=4, row=6)
ttk.Button(root, text="4", command=lambda: write(4)).grid(column=1, row=7)
ttk.Button(root, text="5", command=lambda: write(5)).grid(column=2, row=7)
ttk.Button(root, text="6", command=lambda: write(6)).grid(column=3, row=7)
ttk.Button(root, text="-", command=lambda: write("-")).grid(column=4, row=7)
ttk.Button(root, text="1", command=lambda: write(1)).grid(column=1, row=8)
ttk.Button(root, text="2", command=lambda: write(2)).grid(column=2, row=8)
ttk.Button(root, text="3", command=lambda: write(3)).grid(column=3, row=8)
ttk.Button(root, text="+", command=lambda: write("+")).grid(column=4, row=8)
ttk.Button(root, text="0", command=lambda: write(0)).grid(column=2, row=9)
ttk.Button(root, text=".", command=lambda: write(".")).grid(column=2, row=5)
ttk.Button(root, text="=", command=lambda: calculate()).grid(column=4, row=9)
ttk.Button(root, text="**", command=lambda: write("**")).grid(column=3, row=5)

root.mainloop()