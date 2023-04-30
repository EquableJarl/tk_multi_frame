from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
frame2 = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name", foreground='red', background='blue')
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")
test = ttk.Button(frame2, text="test")
test2 = ttk.Button(frame2, text="test2")
test3 = ttk.Button(frame2, text="test3")
test.pack()
test2.pack()
test3.pack()

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=2, rowspan=2)
frame2.grid(column=6, row=0)
namelbl.grid(column=4, row=0, columnspan=2)
name.grid(column=4, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=4, row=3)
cancel.grid(column=5, row=3)


root.mainloop()