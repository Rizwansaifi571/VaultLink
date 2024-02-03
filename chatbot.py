import tkinter as tk
from tkinter import ttk, scrolledtext
import re
import random

class LoveChatbot:
    def __init__(self):
        self.conversation_history = []

    def save_message(self, user, message):
        self.conversation_history.append((user, message))

    def respond_to_message(self, message):
            intent_handlers = {
                r"(hello|hi|hey)": self.handle_greeting,
                r"search\s+(.*)": self.handle_search,
                r"history": self.handle_history,
                r"advice": self.handle_advice,
                r"weather": self.handle_weather,
                r"(exit|goodbye)": self.handle_goodbye,
                r"(how are you|how do you feel)": self.handle_feelings,
                r"tell me a joke": self.handle_joke,
                r"what's your favorite love story": self.handle_love_story,
                r"compliment me": self.handle_compliment,
                r"what's your dream date": self.handle_dream_date,
                r"express your love": self.handle_express_love,
                r"share a secret": self.handle_secret,
                r"what's the most romantic place": self.handle_romantic_place,
                r"write me a love letter": self.handle_love_letter,
                r"love percentage between (.*) and (.*)": self.handle_love_percentage,
            }

            for pattern, handler in intent_handlers.items():
                match = re.match(pattern, message, re.IGNORECASE)
                if match:
                    return handler(*match.groups())

            return self.handle_default()

    def handle_greeting(self):
        return "Hello, my love! How can I make your heart flutter? 💖"

    def handle_search(self, search_term):
        return f"Searching for '{search_term}'... Results will be displayed shortly. 🌟"

    def handle_history(self):
        history_text = "\n".join(f"{user}: {msg}" for user, msg in self.conversation_history)
        return f"Our Conversation History:\n{history_text} 📜"

    def handle_advice(self):
        return "You are the melody to my heart's song. Share your thoughts, my love. 🎶"

    def handle_weather(self):
        return "Our love forecast is filled with warmth and joy, just like every day with you. ☀️"

    def handle_goodbye(self):
        return "Goodbye, my sweet love! Until our hearts meet again. 💕"

    def handle_feelings(self):
        return "In the symphony of emotions, your love is my favorite tune. Always happy when talking to you. 💬"

    def handle_joke(self):
        return "Why did the two hearts go on a date? Because they wanted to be in sync! 😄"

    def handle_love_story(self):
        return "Our love story is my favorite, written in the stars and filled with endless chapters of joy. 🌌💑"

    def handle_compliment(self):
        return "Your smile could light up the darkest night, and your presence makes every moment special. 😊💖"

    def handle_dream_date(self):
        return "A dream date for us would be a moonlit stroll, sharing sweet whispers and stolen kisses. 🌙💏"

    def handle_express_love(self):
        return "In the garden of my heart, your love blooms like a beautiful flower, filling every moment with joy. 🌹💘"

    def handle_secret(self):
        return "Our love is the most enchanting secret, whispered between the beats of our hearts. 🤫💕"

    def handle_romantic_place(self):
        return "The most romantic place is wherever you are, surrounded by the warmth of your love. 🏞️💑"

    def handle_love_letter(self):
        return "My Dearest, Your love is the poetry of my soul, written in the ink of passion. Forever yours, ❤️"


    def handle_love_percentage(self, names):
        love_percentage = calculate_love_percentage(names[0], names[1])
        romantic_line = get_romantic_line(love_percentage)
        return f"The love percentage between {names[0]} and {names[1]} is {love_percentage}%! 💑 {romantic_line}"

    def respond_to_message(self, message):
        if re.match(r"(hello|hi|hey)", message, re.IGNORECASE):
            return self.handle_greeting()

        elif re.match(r"search\s+(.*)", message, re.IGNORECASE):
            search_term = re.match(r"search\s+(.*)", message, re.IGNORECASE).group(1)
            return self.handle_search(search_term)

        elif re.match(r"history", message, re.IGNORECASE):
            return self.handle_history()

        elif re.match(r"advice", message, re.IGNORECASE):
            return self.handle_advice()

        elif re.match(r"weather", message, re.IGNORECASE):
            return self.handle_weather()

        elif re.match(r"(exit|goodbye)", message, re.IGNORECASE):
            return self.handle_goodbye()

        elif re.match(r"(how are you|how do you feel)", message, re.IGNORECASE):
            return self.handle_feelings()

        elif re.match(r"tell me a joke", message, re.IGNORECASE):
            return self.handle_joke()

        elif re.match(r"what's your favorite love story", message, re.IGNORECASE):
            return self.handle_love_story()

        elif re.match(r"compliment me", message, re.IGNORECASE):
            return self.handle_compliment()

        elif re.match(r"what's your dream date", message, re.IGNORECASE):
            return self.handle_dream_date()

        elif re.match(r"express your love", message, re.IGNORECASE):
            return self.handle_express_love()

        elif re.match(r"share a secret", message, re.IGNORECASE):
            return self.handle_secret()

        elif re.match(r"what's the most romantic place", message, re.IGNORECASE):
            return self.handle_romantic_place()

        elif re.match(r"write me a love letter", message, re.IGNORECASE):
            return self.handle_love_letter()

        elif re.match(r"love percentage between (.*) and (.*)", message, re.IGNORECASE):
            names = re.match(r"love percentage between (.*) and (.*)", message, re.IGNORECASE).groups()
            return self.handle_love_percentage(names)

        else:
            return self.handle_feelings()  # Default response

def calculate_love_percentage(name1, name2):
    random.seed(hash(name1 + name2))
    return random.randint(60, 99)

def get_romantic_line(love_percentage):
    if love_percentage >= 90:
        return "Our love is like a fairytale, destined to last forever."
    elif 70 <= love_percentage < 90:
        return "Every moment with you is a beautiful chapter in our love story."
    else:
        return "Our love is just beginning, like a blossoming flower."

# Create an instance of the LoveChatbot
love_chatbot = LoveChatbot()

class LoveChatApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Love Sanctuary.")

        # Set window dimensions to full screen
        self.state("zoomed")

        # Configure style for themed widgets
        style = ttk.Style()
        style.configure("TFrame", background="#FCE4EC", borderwidth=5, relief="ridge")  # Light Pink theme
        style.configure("TLabel", foreground="#880E4F", font=("Georgia", 16, "italic", "bold"))
        style.configure("TButton", background="#F06292", foreground="white", borderwidth=2, relief="raised", padding=5)
        style.map("TButton", background=[("active", "#E91E63")], foreground=[("active", "black")])

        # Create a themed frame
        self.frame = ttk.Frame(self, style="TFrame", padding="10")
        self.frame.grid(row=1, column=0, sticky="nsew")

        # Title label
        title_label = ttk.Label(self, text="LOVE_SANCTUARY.", style="TLabel")
        title_label.grid(row=0, column=0, padx=10, pady=5, sticky="n")

        # Chat history display with increased width and height
        self.history_display = scrolledtext.ScrolledText(self.frame, width=10, height=33, state="disabled",
                                                         bg="#F8BBD0", font=("Arial", 10))
        self.history_display.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # User input entry with romantic suggestion
        romantic_suggestion = "In the symphony of emotions, your love is my favorite tune. Share your feelings, my dearest. 💬"
        self.user_input_entry = ttk.Entry(self, width=80, font=("Arial", 12), justify="left")
        self.user_input_entry.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
        self.user_input_entry.insert(0, romantic_suggestion)
        self.user_input_entry.bind("<FocusIn>", self.clear_suggestion)

        # Send button
        self.send_button = ttk.Button(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")

        # Make the rows and columns expandable
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(2, weight=1)

    def clear_suggestion(self, event):
        current_text = self.user_input_entry.get()
        romantic_suggestion = "In the symphony of emotions, your love is my favorite tune. Share your feelings, my dearest. 💬"

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
