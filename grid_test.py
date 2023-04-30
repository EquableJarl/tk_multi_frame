import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("1000x750")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)

menuFrame = ttk.Frame(root, border=1, relief="raised" )
menuButton1 = ttk.Button(menuFrame, text="button1")
menuButton2 = ttk.Button(menuFrame, text="button2")
menuButton3 = ttk.Button(menuFrame, text="button3")
menuButton1.pack(side='top', expand='yes')
menuButton2.pack(side='top', expand='yes')
menuButton3.pack(side='top', expand='yes')
menuFrame.grid(row=0, column=0, rowspan=2, columnspan=1, sticky='nsew')

textFrame = ttk.Frame(root, border=1, relief="raised")
textFrame.grid(row=0, column=1, rowspan=1, columnspan=2, sticky='nsew')
textBox = tk.Text(textFrame)
textBox.grid(row=0, column=0, sticky='nsew')

entry = ttk.Entry(root)
entry.grid(row=1, column=1)

button = ttk.Button(text="Click me")
button.grid(row=1, column=2)




# username
# username_label = ttk.Label(root, text="Username:")
# username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

# username_entry = ttk.Entry(root)
# username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# # password
# password_label = ttk.Label(root, text="Password:")
# password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

# password_entry = ttk.Entry(root,  show="*")
# password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# # login button
# login_button = ttk.Button(root, text="Login")
# login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()