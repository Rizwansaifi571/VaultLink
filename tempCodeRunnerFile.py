import tkinter as tk
from tkinter import ttk, scrolledtext
import re

class LifeAdviserChatbot:
    def __init__(self):
        self.search_history = []

    def save_search(self, query):
        self.search_history.append(query)

    def respond_to_query(self, query):
        if re.match(r"(hello|hi|hey)", query, re.IGNORECASE):
            return "Hello! How can I assist you today?"

        elif re.match(r"search\s+(.*)", query, re.IGNORECASE):
            search_term = re.match(r"search\s+(.*)", query, re.IGNORECASE).group(1)
            self.save_search(search_term)
            return f"Searching for '{search_term}'... Results will be displayed shortly."

        elif re.match(r"history", query, re.IGNORECASE):
            history_text = "\n".join(f"You: {search}" for search in self.search_history)
            return f"Search History:\n{history_text}"

        elif re.match(r"advice", query, re.IGNORECASE):
            return "Remember to take breaks, stay hydrated, and focus on the positive aspects of your life."

        elif re.match(r"weather", query, re.IGNORECASE):
            return "The weather today is sunny with a high of 25°C."

        elif re.match(r"(exit|goodbye)", query, re.IGNORECASE):
            return "Goodbye! Have a great day."

        else:
            return "I'm here to chat and offer advice. How can I make your day better?"

# Create an instance of the chatbot
chatbot = LifeAdviserChatbot()

class ChatApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Life Adviser Chatbot")
        self.geometry("600x400")  # Set window dimensions

        # Configure style for themed widgets
        style = ttk.Style()
        style.configure("TFrame", background="#2E3B4E", borderwidth=5, relief="ridge")  # Dark Blue theme
        style.configure("TLabel", background="#2E3B4E", foreground="white")
        style.configure("TButton", background="#4A90E2", foreground="white", borderwidth=2, relief="raised", padding=5)
        style.map("TButton", background=[("active", "#2E3B4E")], foreground=[("active", "white")])

        # Create a themed frame
        self.frame = ttk.Frame(self, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Chat history display
        self.history_display = scrolledtext.ScrolledText(self.frame, width=50, height=10, state="disabled")
        self.history_display.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

        # User input entry
        self.user_input_entry = ttk.Entry(self.frame, width=40)
        self.user_input_entry.grid(row=1, column=0, pady=10, sticky="nsew")

        # Send button
        self.send_button = ttk.Button(self.frame, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, pady=10, sticky="nsew")

        # Make the rows and columns expandable
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def send_message(self):
        user_input = self.user_input_entry.get()

        # Update history display
        self.history_display.config(state="normal")
        self.history_display.insert(tk.END, f"You: {user_input}\nBot: {chatbot.respond_to_query(user_input)}\n")
        self.history_display.config(state="disabled")

        # Clear user input entry
        self.user_input_entry.delete(0, tk.END)

# Create an instance of the ChatApplication
app = ChatApplication()
app.mainloop()
