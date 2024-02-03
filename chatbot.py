import tkinter as tk
from tkinter import ttk, scrolledtext
import re

class LoveChatbot:
    def __init__(self):
        self.conversation_history = []

    def save_message(self, user, message):
        self.conversation_history.append((user, message))

    def respond_to_message(self, message):
        if re.match(r"(hello|hi|hey)", message, re.IGNORECASE):
            return "Hello, my love! How can I make your heart flutter?"

        elif re.match(r"search\s+(.*)", message, re.IGNORECASE):
            search_term = re.match(r"search\s+(.*)", message, re.IGNORECASE).group(1)
            return f"Searching for '{search_term}'... Results will be displayed shortly."

        elif re.match(r"history", message, re.IGNORECASE):
            history_text = "\n".join(f"{user}: {msg}" for user, msg in self.conversation_history)
            return f"Our Conversation History:\n{history_text}"

        elif re.match(r"advice", message, re.IGNORECASE):
            return "You are the melody to my heart's song. Share your thoughts, my love."

        elif re.match(r"weather", message, re.IGNORECASE):
            return "Our love forecast is filled with warmth and joy, just like every day with you."

        elif re.match(r"(exit|goodbye)", message, re.IGNORECASE):
            return "Goodbye, my sweet love! Until our hearts meet again."

        else:
            return "In the symphony of emotions, your love is my favorite tune. Share your feelings, my dearest."

# Create an instance of the LoveChatbot
love_chatbot = LoveChatbot()

class LoveChatApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Love Sanctuary.")
        self.geometry("800x500")  # Set window dimensions

        # Configure style for themed widgets
        style = ttk.Style()
        style.configure("TFrame", background="#FFB6C1", borderwidth=5, relief="ridge")  # Light Pink theme
        style.configure("TLabel", foreground="#800000", font=("Helvetica", 16, "italic", "bold"))
        style.configure("TButton", background="#FF69B4", foreground="white", borderwidth=2, relief="raised", padding=5)
        style.map("TButton", background=[("active", "pink")], foreground=[("active", "black")])

        # Create a themed frame
        self.frame = ttk.Frame(self, style="TFrame", padding="10")
        self.frame.grid(row=1, column=0, sticky="nsew")

        # Title label
        title_label = ttk.Label(self, text="Love Sanctuary.", style="TLabel")
        title_label.grid(row=0, column=0, padx=10, pady=5, sticky="n")

        # Chat history display
        self.history_display = scrolledtext.ScrolledText(self.frame, width=60, height=12, state="disabled",
                                                         bg="#FFEBEE", font=("Arial", 10))
        self.history_display.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # User input entry with romantic suggestion
        romantic_suggestion = "In the symphony of emotions, your love is my favorite tune. Share your feelings, my dearest."
        self.user_input_entry = ttk.Entry(self, width=150, font=("Arial", 12), justify="left")
        self.user_input_entry.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.user_input_entry.insert(0, romantic_suggestion)
        self.user_input_entry.bind("<FocusIn>", self.clear_suggestion)

        # Send button
        self.send_button = ttk.Button(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        # Make the rows and columns expandable
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def clear_suggestion(self, event):
        current_text = self.user_input_entry.get()
        romantic_suggestion = "In the symphony of emotions, your love is my favorite tune. Share your feelings, my dearest."

        if current_text == romantic_suggestion:
            self.user_input_entry.delete(0, tk.END)

    def send_message(self):
        user_input = self.user_input_entry.get()

        # Update history display
        love_chatbot.save_message("You", user_input)
        response = love_chatbot.respond_to_message(user_input)

        self.history_display.config(state="normal")
        self.history_display.insert(tk.END, f"You: {user_input}\nMy Love: {response}\n")
        self.history_display.config(state="disabled")

        # Clear user input entry
        self.user_input_entry.delete(0, tk.END)

# Create an instance of the LoveChatApplication
love_app = LoveChatApplication()
love_app.mainloop()
