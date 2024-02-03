import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VaultLinkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VaultLink - Your Financial Companion")

        # Set a more luxurious color palette
        background_color = "#2c3e50"
        accent_color = "#3498db"
        button_color = "#e74c3c"  # Updated button color
        header_color = "#ecf0f1"

        # Set clean and readable fonts
        font_style = ("Arial", 12)

        # Main window background color
        self.root.configure(bg=background_color)

        # Create a top menu for navigation
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Create menu items for different sections
        self.dashboard_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.dashboard_menu.add_command(label="Dashboard")
        self.menu_bar.add_cascade(label="Dashboard", menu=self.dashboard_menu)

        self.banking_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.banking_menu.add_command(label="Banking")
        self.menu_bar.add_cascade(label="Banking", menu=self.banking_menu)

        self.expenses_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.expenses_menu.add_command(label="Expenses")
        self.menu_bar.add_cascade(label="Expenses", menu=self.expenses_menu)

        # Create a frame for the main content with borders
        self.main_frame = ttk.Frame(root, padding=(20, 20, 20, 20), style="Main.TFrame", borderwidth=2, relief="solid")
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add a header with application name and logo
        header_label = ttk.Label(self.main_frame, text="VaultLink", font=("Arial", 32, "bold"), background=header_color, foreground=accent_color)
        header_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Create buttons with a more sophisticated style and appropriate size
        dashboard_button = ttk.Button(self.main_frame, text="Dashboard", command=self.dummy_function, style="ActionButton.TButton", width=20)
        dashboard_button.grid(row=1, column=0, pady=(0, 10))

        banking_button = ttk.Button(self.main_frame, text="Banking", command=self.dummy_function, style="ActionButton.TButton", width=20)
        banking_button.grid(row=2, column=0, pady=(0, 10))

        expenses_button = ttk.Button(self.main_frame, text="Expenses", command=self.dummy_function, style="ActionButton.TButton", width=20)
        expenses_button.grid(row=3, column=0, pady=(0, 10))

        # Create a button to switch to the AuthenticationFrame
        auth_button = ttk.Button(self.main_frame, text="Login", command=self.show_authentication_frame, style="AuthButton.TButton", width=20)
        auth_button.grid(row=4, column=0, pady=(10, 0))

        # Initialize AuthenticationFrame
        self.authentication_frame = AuthenticationFrame(self.root, self.hide_authentication_frame)

    def show_authentication_frame(self):
        self.main_frame.grid_forget()
        self.authentication_frame.show_frame()

    def hide_authentication_frame(self):
        self.authentication_frame.hide_frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")

    def dummy_function(self):
        pass

class AuthenticationFrame:
    def __init__(self, root, on_close_callback):
        self.root = root
        self.on_close_callback = on_close_callback

        # Create a frame for authentication
        self.auth_frame = ttk.Frame(root, padding=(20, 20, 20, 20), style="Auth.TFrame", borderwidth=2, relief="solid")
        self.auth_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.auth_frame.grid_forget()

        # Add a header with authentication title
        auth_header_label = ttk.Label(self.auth_frame, text="User Authentication", font=("Arial", 24, "bold"), background="#ecf0f1", foreground="#3498db")
        auth_header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Add username and password labels and entry widgets
        ttk.Label(self.auth_frame, text="Username:", font=("Arial", 12), background="#ecf0f1").grid(row=1, column=0, pady=(0, 10))
        self.username_entry = ttk.Entry(self.auth_frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=(0, 10))

        ttk.Label(self.auth_frame, text="Password:", font=("Arial", 12), background="#ecf0f1").grid(row=2, column=0, pady=(0, 10))
        self.password_entry = ttk.Entry(self.auth_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, pady=(0, 10))

        # Add a login button with updated color
        login_button = ttk.Button(self.auth_frame, text="Login", command=self.authenticate_user, style="AuthButton.TButton")
        login_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        # Add a "Forgot Password" link
        forgot_password_link = ttk.Label(self.auth_frame, text="Forgot Password?", font=("Arial", 12), background="#ecf0f1", foreground="#3498db", cursor="hand2")
        forgot_password_link.grid(row=4, column=0, columnspan=2, pady=(10, 20))
        forgot_password_link.bind("<Button-1>", self.show_forgot_password_frame)

        # Initialize ForgotPasswordFrame
        self.forgot_password_frame = ForgotPasswordFrame(root, self.hide_forgot_password_frame)

    def show_frame(self):
        self.auth_frame.grid(row=0, column=0, sticky="nsew")

    def hide_frame(self):
        self.auth_frame.grid_forget()

    def show_forgot_password_frame(self, event):
        self.auth_frame.grid_forget()
        self.forgot_password_frame.show_frame()

    def hide_forgot_password_frame(self):
        self.forgot_password_frame.hide_frame()
        self.auth_frame.grid(row=0, column=0, sticky="nsew")

    def authenticate_user(self):
        # Placeholder for authentication logic
        # In a real application, replace this with a secure authentication mechanism
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy authentication check (replace with your authentication logic)
        if username == "user" and password == "password":
            messagebox.showinfo("Authentication", "Login successful!")
            self.on_close_callback()
        else:
            messagebox.showerror("Authentication Error", "Invalid username or password. Please try again.")

class ForgotPasswordFrame:
    def __init__(self, root, on_close_callback):
        self.root = root
        self.on_close_callback = on_close_callback

        # Create a frame for forgot password
        self.forgot_password_frame = ttk.Frame(root, padding=(20, 20, 20, 20), style="Auth.TFrame", borderwidth=2, relief="solid")
        self.forgot_password_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.forgot_password_frame.grid_forget()

        # Add a header with forgot password title
        forgot_password_header_label = ttk.Label(self.forgot_password_frame, text="Forgot Password", font=("Arial", 24, "bold"), background="#ecf0f1", foreground="#3498db")
        forgot_password_header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Add instructions and entry widget for email
        ttk.Label(self.forgot_password_frame, text="Enter your email:", font=("Arial", 12), background="#ecf0f1").grid(row=1, column=0, pady=(0, 10))
        self.email_entry = ttk.Entry(self.forgot_password_frame, font=("Arial", 12))
        self.email_entry.grid(row=1, column=1, pady=(0, 10))

        # Add a submit button with updated color
        submit_button = ttk.Button(self.forgot_password_frame, text="Submit", command=self.dummy_forgot_password, style="AuthButton.TButton")
        submit_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    def show_frame(self):
        self.forgot_password_frame.grid(row=0, column=0, sticky="nsew")

    def hide_frame(self):
        self.forgot_password_frame.grid_forget()

    def dummy_forgot_password(self):
        # Placeholder for forgot password logic
        print("Submitting forgot password request...")

if __name__ == "__main__":
    root = tk.Tk()
    app = VaultLinkApp(root)

    # Configure styles
    style = ttk.Style()
    style.configure("Main.TFrame", background="#2c3e50")
    style.configure("ActionButton.TButton", background="#27ae60", foreground="#ffffff", font=("Arial", 12, "bold"))
    style.configure("Auth.TFrame", background="#ecf0f1")
    style.configure("AuthButton.TButton", background="#e74c3c", foreground="#ffffff", font=("Arial", 12, "bold"))  # Updated button color

    root.geometry("600x400")  # Set your preferred window size
    root.mainloop()
