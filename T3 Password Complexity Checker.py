import re
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess password strength based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Moderate"
    else:
        return "Weak"

def check_password_strength():
    password = entry_password.get()
    strength = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

def toggle_password_visibility():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# Create Tkinter window
window = tk.Tk()
window.title("Password Strength Assessment Tool")

# Create labels and entry widget for password
label_password = tk.Label(window, text="Enter your password:")
label_password.grid(row=0, column=0, padx=10, pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.grid(row=0, column=1, padx=10, pady=5)

# Create checkbox to toggle password visibility
show_password_var = tk.BooleanVar()
checkbox_show_password = tk.Checkbutton(window, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
checkbox_show_password.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Create button to check password strength
button_check = tk.Button(window, text="Check Strength", command=check_password_strength)
button_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Run Tkinter event loop
window.mainloop()
