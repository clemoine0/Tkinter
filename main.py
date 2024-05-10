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

# FRAMES
title_frame = tk.Frame(top)
top_frame = tk.Frame(top,relief="sunken", border=10)
frame1 = tk.Frame(top_frame, relief="raised", border=10)
frame2 = tk.Frame(top_frame, relief="raised", border=10)
bottom_frame= tk.Frame(top,relief="sunken",border=10)

# ELEMENTS
button1 = tk.Button(frame1, text="button1", command=helloCallBack)
button2 = tk.Button(frame1, text="button2")
button3 = tk.Button(bottom_frame, text="bottom")

listbox = tk.Listbox(bottom_frame)
listbox.insert(1, "first")
listbox.insert(2, "second")

label2_text = tk.StringVar()
label2_text.set("OFF")

# checkbutton_var2 = tk.IntVar()

checkbutton1 = tk.Checkbutton(frame2, text="Music",variable=label2_text,onvalue="ON",offvalue="OFF",height=2,width=20)
entry1 = tk.Entry(frame2)
label1 = tk.Label(frame2,text="Playlist Name")
label2 = tk.Label(bottom_frame,textvariable=label2_text)
title = tk.Label(title_frame,text="hallo",pady=15)

# PACKING + LOOP
title_frame.pack()
title.pack()
top_frame.pack(fill="x",side="top")
frame1.pack(fill="both",side="left", expand=True)
button1.pack()
button2.pack()
frame2.pack(fill="both",side="right",expand=True)
checkbutton1.pack()
label1.pack()
entry1.pack()
bottom_frame.pack(fill="x",side="bottom")
label2.pack()
button3.pack()
listbox.pack()


top.mainloop()
