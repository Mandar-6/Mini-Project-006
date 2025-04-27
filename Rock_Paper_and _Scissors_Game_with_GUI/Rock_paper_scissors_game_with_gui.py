import tkinter as tk
from PIL import Image, ImageTk
import random

# Basic Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("1920x1080")

# Load Images
rock_img = ImageTk.PhotoImage(Image.open("C:/Users/User/Downloads/rock.png").resize((150,150), Image.LANCZOS))
paper_img = ImageTk.PhotoImage(Image.open("C:/Users/User/Downloads/paper.png").resize((150,150), Image.LANCZOS))
scissors_img = ImageTk.PhotoImage(Image.open("C:/Users/User/Downloads/scissor.png").resize((150,150), Image.LANCZOS))

heading = tk.Label(root, text="Welcome to the Rock, Paper, and Scissors Game!", font=("Broadway", 14))
heading.pack(pady=10)
heading_2 = tk.Label(root, text="Choose from the below buttons and keep playing!", font=("Arial", 10))
heading_2.pack(pady=15)
# Functions
def user_choice(choice):
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    show_choices(choice, computer)
    decide_winner(choice, computer)

def show_choices(user, computer):
    if user == "rock":
        user_label.config(image=rock_img)
        user_text.config(text="You choose Rock", font=("Arial",9))
    elif user == "paper":
        user_label.config(image=paper_img)
        user_text.config(text="You choose Paper", font=("Arial",9))
    else:
        user_label.config(image=scissors_img)
        user_text.config(text="You choose Scissors", font=("Arial",9))

    if computer == "rock":
        comp_label.config(image=rock_img)
        comp_text.config(text="Computer choose Rock", font=("Arial",9))
    elif computer == "paper":
        comp_label.config(image=paper_img)
        comp_text.config(text="Computer choose Paper", font=("Arial",9))
    else:
        comp_label.config(image=scissors_img)
        comp_text.config(text="Computer choose Scissors", font=("Arial",9))

def decide_winner(user, computer):
    if user == computer:
        result.config(text="It's a draw!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        result.config(text="You win!")
    else:
        result.config(text="You lose!")

# Labels to show choices
user_label = tk.Label(root)
user_label.pack(pady=20)
user_text = tk.Label(root, text="")
user_text.pack(pady=5)

comp_label = tk.Label(root)
comp_label.pack(pady=20)
comp_text = tk.Label(root, text="")
comp_text.pack(pady=5)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice("rock"))
rock_button.grid(row=0, column=0, padx=20)
rock_button.config(bg="Gray")

paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice("paper"))
paper_button.grid(row=0, column=1, padx=20)
paper_button.config(bg="honeydew2")

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=20)
scissors_button.config(bg="Yellow")

# Label to show result
result = tk.Label(root, text="", font=("Arial", 20))
result.pack(pady=20)

root.mainloop()







