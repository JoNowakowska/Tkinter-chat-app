import tkinter as tk
from tkinter import ttk
import requests
from frames.message_bubble import MessageBubble

messages = [{'date': 5555333344, 'message': 'Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !Good night Good night !'}]


class Chat(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.messages_window = MessageBubble(self)
        self.messages_window.grid(row=0, column=0, sticky = 'nswe')

        self.message_labels = []

        self.messages_window.show_messages(messages, self.message_labels)

        input_frame = ttk.Frame(self)
        input_frame.grid(row=1, column=0, sticky = 'we')

        self.text_window = tk.Text(
            input_frame,
            height = 4
        )

        self.text_window.pack(fill='both', side = 'left', expand=True, padx = (0,10))

        fetch_button = ttk.Button(
            input_frame,
            text = 'Fetch',
            cursor = 'hand2',
            command = self.get_messages
        )

        fetch_button.pack()

        send_button = ttk.Button(
            input_frame,
            text = 'Send',
            cursor = 'hand2',
            command = self.post_messages
        )

        send_button.pack()

    def get_messages(self):
        global messages
        messages = requests.get('http://167.99.63.70/messages').json()
        self.messages_window.show_messages(messages, self.message_labels)
        self.after(150, lambda: self.messages_window.yview_moveto(1.0))
    
    def post_messages(self):
        body = self.text_window.get('1.0', 'end').strip()
        requests.post('http://167.99.63.70/message', json = {'message': body})
        self.text_window.delete('1.0', 'end')
        self.get_messages()