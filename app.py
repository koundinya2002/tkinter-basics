import tkinter as tk
from tkinter import messagebox


class myGUI():
    
    def __init__(self):
        self.root = tk.Tk()

        self.menuBar = tk.Menu(self.root)
        self.actionMenu = tk.Menu(self.root)

        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label='close', command=self.on_closing)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="close without questioning", command=exit)

        self.actionMenu = tk.Menu(self.actionMenu, tearoff=0)
        self.actionMenu.add_command(label='show message', command=self.show_message)

        self.menuBar.add_cascade(menu=self.fileMenu, label="File")
        self.menuBar.add_cascade(menu=self.actionMenu, label="Action")
        self.root.config(menu=self.menuBar)

        self.label = tk.Label(self.root, text="Your Message:", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.value_Entry = tk.Entry(self.root, font=('Arial', 16))
        self.value_Entry.bind('<KeyPress>', self.shortcuts)
        self.value_Entry.pack(padx=10, pady=10)

        self.clearBtn = tk.Button(self.root, text="Clear", font=('Arial', 16), command=self.clear)
        self.clearBtn.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Click to display yout message", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show your message:", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get()==1:
            messagebox.showinfo(title="Message Box", message=self.value_Entry.get())
        else:
            print("Please check the box!")

    def shortcuts(self, event):
        if (event.keysym=="Return" and event.state==8):
            self.show_message

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.value_Entry.delete('1.0', tk.END)
myGUI()