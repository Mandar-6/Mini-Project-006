import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    # Get the number of characters, numbers, and symbols from the user
    try:
        num_letters = int(letters_entry.get()) if letters_entry.get() else 0
        num_numbers = int(numbers_entry.get()) if numbers_entry.get() else 0
        num_symbols = int(symbols_entry.get()) if symbols_entry.get() else 0
        if num_letters == 0 and num_numbers == 0 and num_symbols == 0:
            password_label.config(text="Please enter value for at least one category!", font=("Arial", 10))
            return None
    except ValueError:
        password_label.config(text="Enter a valid value", font=("Arial", 10))
        return None

    # Create a pool of characters
    letters = string.ascii_letters  # All lowercase and uppercase letters
    numbers = string.digits          # All digits (0-9)
    symbols = string.punctuation     # All punctuation symbols

    # Initialize an empty list to store the password characters
    password = []

    # Add the requested number of letters, numbers, and symbols to the password list
    password += random.choices(letters, k=num_letters)
    password += random.choices(numbers, k=num_numbers)
    password += random.choices(symbols, k=num_symbols)

    # Shuffle the list to ensure the characters are randomized
    random.shuffle(password)

    # Convert the list to a string and display the password
    password = ''.join(password)
    password_label.config(text=f"Your generated password is: {password}")
    return password

def copy_password():
    password = generate_password()
    if password:
        pyperclip.copy(password)
        label_copy_status.config(text="Password copied to clipboard", font=("Arial", 10) , fg="green")
    else:
        label_copy_status.config(text="No password to copy", font=("Arial", 10), fg="red")

# Set up the Tkinter window
root = tk.Tk()
root.title("Password Generator App")
root.geometry("500x500")

# Heading
heading = tk.Label(root, text="Password Generator", font=("Times New Roman", 16))
heading.pack(pady=10)

# Labels and Entries for input
letters_label = tk.Label(root, text="Number of Letters:")
letters_label.pack(pady=5)
letters_entry = tk.Entry(root, width=10, font=("Arial", 14))
letters_entry.pack(pady=5)

numbers_label = tk.Label(root, text="Number of Numbers:")
numbers_label.pack(pady=5)
numbers_entry = tk.Entry(root, width=10, font=("Arial", 14))
numbers_entry.pack(pady=5)

symbols_label = tk.Label(root, text="Number of Symbols:")
symbols_label.pack(pady=5)
symbols_entry = tk.Entry(root, width=10, font=("Arial", 14))
symbols_entry.pack(pady=5)

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), command = generate_password)
generate_button.pack(pady=20)

# Label to display the generated password
password_label = tk.Label(root, text="Your generated password:", font=("Arial", 14))
password_label.pack(pady=10)

# Button to copy the password to clipboard
generate_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 14), command = copy_password)
generate_button.pack(pady=20)

# Label to display for copy clipboard
label_copy_status = tk.Label(root, text="", font=("Arial", 12))
label_copy_status.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
