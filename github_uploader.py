# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:39:32 2024

@author: pnienaltowski
"""
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from github import Github
import os

# File to store the token
TOKEN_FILE = "github_token.txt"

def load_token():
    """Load the GitHub token from the local file."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_token(token):
    """Save the GitHub token to the local file."""
    with open(TOKEN_FILE, "w") as f:
        f.write(token)

def upload_to_github():
    token = token_entry.get().strip()
    repo_name = repo_entry.get().strip()
    branch = branch_entry.get().strip()
    file_path = file_path_entry.get().strip()
    commit_message = commit_entry.get().strip()

    if not token or not repo_name or not branch or not file_path or not commit_message:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    # Save the token for future sessions
    save_token(token)

    try:
        # Initialize GitHub instance
        g = Github(token)
        repo = g.get_repo(repo_name)

        # Define the path in the repo where the file will be uploaded
        file_in_repo = os.path.basename(file_path)

        try:
            # Try to get the contents of the file to check if it exists
            contents = repo.get_contents(file_in_repo, ref=branch)
            # If file exists, update it
            repo.update_file(contents.path, commit_message, open(file_path, "r").read(), contents.sha, branch=branch)
            messagebox.showinfo("Success", f"Updated {file_in_repo} in the repository {repo_name}.")
        except:
            # If file does not exist, create it
            repo.create_file(file_in_repo, commit_message, open(file_path, "r").read(), branch=branch)
            messagebox.showinfo("Success", f"Uploaded {file_in_repo} to the repository {repo_name}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

def on_close():
    """Close the application."""
    root.quit()
    root.destroy()

# Function to create a rounded button
def create_rounded_button(canvas, x, y, width, height, radius, text, command, bg, fg):
    # Draw rounded button background
    canvas.create_oval(x, y, x + radius * 2, y + radius * 2, fill=bg, outline=bg)
    canvas.create_oval(x + width - radius * 2, y, x + width, y + radius * 2, fill=bg, outline=bg)
    canvas.create_rectangle(x + radius, y, x + width - radius, y + radius * 2, fill=bg, outline=bg)

    # Create the actual button
    button = Button(
        root,
        text=text,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        bd=0,
        highlightthickness=0,
        command=command,
        font=("Helvetica", 12),
    )

    # Place the button in the canvas
    button_window = canvas.create_window(x + width / 2, y + radius, window=button, anchor="center")
    return button_window

# Main GUI window
root = Tk()
root.title("GitHub File Uploader")
root.geometry("500x420")
root.configure(bg="#353839")

# Create Canvas for Buttons
canvas = Canvas(root, bg="#353839", highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

# Load the saved token
saved_token = load_token()

# Add Title
title_label = Label(
    root,
    text="GitHub Uploader",
    font=("Consolas", 20, "bold"),
    bg="#353839",
    fg="#F0EFF4",
)
title_label.place(relx=0.5, y=30, anchor=CENTER)

# Section 1: GitHub Parameters
section_1_label = tk.Label(root, text="GitHub Parameters", font=("Helvetica", 14), bg="#353839", fg="#EF767A")
section_1_label.place(x=20, y=70)

tk.Label(root, text="GitHub Token:", bg="#353839", fg="#F0EFF4").place(x=70, y=110)
token_entry = tk.Entry(root, width=50, bg="#F0EFF4", fg="#353839")
token_entry.insert(0, saved_token)  # Pre-fill with the saved token
token_entry.place(x=150, y=110)

tk.Label(root, text="Repo Name:", bg="#353839", fg="#F0EFF4").place(x=80, y=150)
repo_entry = tk.Entry(root, width=50, bg="#F0EFF4", fg="#353839")
repo_entry.place(x=150, y=150)

tk.Label(root, text="Branch:", bg="#353839", fg="#F0EFF4").place(x=105, y=190)
branch_entry = tk.Entry(root, width=50, bg="#F0EFF4", fg="#353839")
branch_entry.place(x=150, y=190)

# Separator
separator = ttk.Separator(root, orient="horizontal")
separator.place(x=0, y=230, width=660)

# Section 2: File and Commit Message
section_2_label = tk.Label(root, text="File Upload and Commit Message", font=("Helvetica", 14), bg="#353839", fg="#EF767A")
section_2_label.place(x=20, y=250)

# File Path Entry
tk.Label(root, text="File Path:", bg="#353839", fg="#F0EFF4").place(x=96, y=290)
file_path_entry = tk.Entry(root, width=41, bg="#F0EFF4", fg="#353839")  # Shorter entry field
file_path_entry.place(x=150, y=290)

browse_button = tk.Button(
    root, text="Browse", command=browse_file, bg="#EEDC82", fg="#353839", bd=0, activebackground="#EEDC82"
)
browse_button.place(x=410, y=288)  # Positioned right next to the entry

tk.Label(root, text="Message:", bg="#353839", fg="#F0EFF4").place(x=96, y=330)
commit_entry = tk.Entry(root, width=50, bg="#F0EFF4", fg="#353839")
commit_entry.place(x=150, y=330)

# Rounded Buttons
button_width = 100  # Reduced width
button_height = 30  # Reduced height
button_radius = 15  # Smaller radius

create_rounded_button(
    canvas,
    130,  # Moved closer to the left
    370,  # Adjusted y-position
    button_width,
    button_height,
    button_radius,
    text="upload",
    command=upload_to_github,
    bg="#28A745",  # Green for Upload
    fg="#353839",
)

create_rounded_button(
    canvas,
    250,  # Positioned closer to Upload
    370,  # Same y-position
    button_width,
    button_height,
    button_radius,
    text="exit",
    command=on_close,
    bg="#DC3545",  # Red for Exit
    fg="#353839",
)

# Start the GUI event loop
root.mainloop()





