import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1000x750")

root.rowconfigure(0, weight= 2)
root.rowconfigure(1, weight= 3)
root.rowconfigure(2, weight= 2)

for column in range(8):
    root.columnconfigure(column, weight=1)

top_frame = ttk.Frame()
top_frame_style = ttk.Style()
top_frame_style.configure("TFrame", background='red')
top_frame.grid(row=0, column=0, rowspan=1, columnspan=8, sticky="NSEW")

for row in range(3):
    top_frame.rowconfigure(row, weight=1)
for column in range(3):
    top_frame.columnconfigure(column, weight=1)


topLabel = ttk.Label(top_frame, text="This is the top label", foreground="blue", )
topLabel.grid(row=1, column=1)

text_frame = tk.Text(root)
text_frame.grid(row=1, column=1, columnspan=6, sticky="NESW")

button1 = ttk.Button(root, text = "this is the text")
button1.grid(row=2, column=0, columnspan=2)

button2 = ttk.Button(root, text = "Button2")
button2.grid(row=2, column=2, columnspan=2)

button3 = ttk.Button(root, text = "button3")
button3.grid(row=2, column=4, columnspan=2)

button4 = ttk.Button(root, text = "Button4")
button4.grid(row=2, column=6, columnspan=2)

root.mainloop()



