import tkinter as tk
from tkinter import messagebox

# CONSTANTS
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300

# FUNCTIONS
def helloCallBack():
    messagebox.showinfo("g")

# WINDOW
top = tk.Tk()
top.minsize(200,200)

# ELEMENTS
button1 = tk.Button(top, text="buttom1", command=helloCallBack)
button2 = tk.Button(top, text="buttom2")

checkbutton_var1 = tk.IntVar()
# checkbutton_var2 = tk.IntVar()
checkbutton1 = tk.Checkbutton(top, text="Music",variable=checkbutton_var1,onvalue=1,offvalue=0,height=2,width=20)
entry1 = tk.Entry(top)
label1 = tk.Label(top,text="Playlist Name")

# PACKING + LOOP
button1.pack()
button2.pack()
checkbutton1.pack()
label1.pack()
entry1.pack()

top.mainloop()
