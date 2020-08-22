import tkinter as tk
from tkinter import ttk
import requests
import datetime
from PIL import Image, ImageTk

MAX_MESSAGE_WIDTH = 800

class MessageBubble(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness = 0)

        self.message_frame = ttk.Frame(self)
        self.message_frame.columnconfigure(0, weight = 1)

        self.scrollable_window = self.create_window((0,0), window = self.message_frame, anchor = 'nw')

        def configure_scroll_region(event):
            self.configure(scrollregion = self.bbox('all'))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width = self.winfo_width())

        self.bind("<Configure>", configure_window_size)

        self.message_frame.bind("<Configure>", configure_scroll_region)

        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient='vertical', command = self.yview)
        scrollbar.grid(row=0, column = 1, sticky= 'ns')

        self.configure(yscrollcommand = scrollbar.set)
        self.yview_moveto(1.0)

    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), 'units')

    
    def show_messages(self, messages, message_labels):
        
        existing_messages = [(date['text'], message['text']) for date, message in message_labels]
        
        for message in messages:
            msg_date = datetime.datetime.fromtimestamp(message['date']).strftime('%d-%m-%Y %H:%M:%S')
            if (msg_date, message['message']) not in existing_messages:

                container = ttk.Frame(self.message_frame)
                container.grid(padx = (10,100), pady=10, sticky = 'ew')
                container.columnconfigure(1, weight = 1)

                def reconfigure_message_labels(event):
                    for _, label in message_labels:
                        label.configure(wraplength = min(container.winfo_width() - 230, MAX_MESSAGE_WIDTH))
                
                container.bind("<Configure>", reconfigure_message_labels)

                date_label = ttk.Label(
                    container,
                    text = msg_date
                )
                date_label.grid(row = 0, column=1, sticky = 'new')

                message_label = ttk.Label(
                    container,
                    text = message['message'], 
                    justify = 'left',
                    anchor = 'w'
                )
                message_label.grid(row = 1, column=1, sticky = 'ewsn')

                avatar = Image.open('./JKN on the beach.png')
                avatar_tk = ImageTk.PhotoImage(avatar)

                avatar_label = ttk.Label(
                    container,
                    image = avatar_tk
                )
                avatar_label.image = avatar_tk
                avatar_label.grid(row = 0 , rowspan = 2, column = 0)
                
                
                message_labels.append((date_label, message_label))