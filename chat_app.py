import tkinter as tk
from tkinter import ttk
from frames import Chat

class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1200x800")
        self.minsize(100, 100)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(self)
        self.chat_frame.grid(padx = 0, pady=10, sticky = 'nwes')


messenger = Messenger()

messenger.mainloop()
