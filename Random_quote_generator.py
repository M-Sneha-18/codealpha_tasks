import tkinter as tk
import random

# Sample quotes
quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "Believe you can and you’re halfway there.",
    "Dream big and dare to fail.",
    "If you want to shine like a sun, first burn like a sun.",
    "If you fail, never give up because F.A.I.L. means 'First Attempt In Learning.'",
    "Life is what happens when you're busy making other plans.",
    "Strive for progress, not perfection.",
    "Either you run the day, or the day runs you.",
    "Be the change that you wish to see in the world.",
    "In the middle of every difficulty lies opportunity.",
    "The only thing we have to fear is fear itself.",
    "That’s one small step for man, one giant leap for mankind.",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
    "The unexamined life is not worth living.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "Do what you can, with what you have, where you are.",
    "Whether you think you can or you think you can’t, you’re right.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Happiness depends upon ourselves.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Imagination is more important than knowledge.",
    "It does not matter how slowly you go as long as you do not stop.",
    "You miss 100% of the shots you don’t take.",
    "Stay hungry, stay foolish.",
    "He who opens a school door, closes a prison.",
    "Knowledge speaks, but wisdom listens.",
    "A person who won’t read has no advantage over one who can’t read.",
    "Education is the Weapon which is used to unlock the door called Knowledge.",
    "Happiness depends upon ourselves.",
    "Not all those who wander are lost.",
    "The journey of a thousand miles begins with one step.",
    "Injustice anywhere is a threat to justice everywhere.",
    "Float like a butterfly, sting like a bee.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall."
]

# Colors for the quote text
colors = ["blue", "red", "green", "black", "purple", "yellow", "orange", "skyblue",
          "pink", "royalblue", "grey", "maroon", "violet", "darkgreen", "cyan", "magenta", "brown", "beige","lime","gold","salmon","navy","teal","Turquoise"]
# Initialize previous values to avoid repetition
last_quote = ""
last_color = ""

# Function to display a random quote in a random color (background stays white)
def display_quote():
    global last_quote, last_color

    quote = random.choice(quotes)
    color = random.choice(colors)

    # Ensure new quote and color are not repeated consecutively
    while quote == last_quote:
        quote = random.choice(quotes)
    while color == last_color:
        color = random.choice(colors)

    last_quote = quote
    last_color = color

    quote_label.config(text=quote, fg=color)
    share_label.config(text="")  # Clear status message

# Function to auto-rotate the quote every 5 seconds
def auto_rotate():
    display_quote()
    root.after(5000, auto_rotate)

# Function to copy the current quote to clipboard
def share_quote():
    current_quote = quote_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(current_quote)
    root.update()
    share_label.config(text="Quote copied to clipboard!", fg="green")

# Function to save quote to a file
def save_quote():
    current_quote = quote_label.cget("text")
    with open("saved_quotes.txt", "a", encoding="utf-8") as file:
        file.write(current_quote + "\n")
    share_label.config(text="Quote saved to file!", fg="blue")

# Create the main window
root = tk.Tk()
root.title("🎨 Colorful Quote Generator")
root.geometry("700x400")
root.config(bg="white")

# Quote label
quote_label = tk.Label(
    root,
    text="Click 'New Quote' to get inspired!",
    wraplength=600,
    justify="center",
    font=("Times New Roman", 16, "italic"),
    bg="white",
    fg="black"
)
quote_label.pack(pady=30)

# New Quote button
new_quote_btn = tk.Button(
    root,
    text="New Quote",
    command=display_quote,
    font=("Times New Roman", 12, "bold"),
    fg="white",
    bg="#4caf50",
    padx=10,
    pady=5
)
new_quote_btn.pack(pady=5)

# Share Quote button
share_btn = tk.Button(
    root,
    text="Share Quote",
    command=share_quote,
    font=("Times New Roman", 12),
    fg="white",
    bg="#2196f3",
    padx=10,
    pady=5
)
share_btn.pack(pady=5)

# Save Quote button
save_btn = tk.Button(
    root,
    text="Save Quote",
    command=save_quote,
    font=("Times New Roman", 12),
    fg="white",
    bg="#9c27b0",
    padx=10,
    pady=5
)
save_btn.pack(pady=5)

# Status label
share_label = tk.Label(
    root,
    text="",
    font=("Times New Roman", 10),
    bg="white"
)
share_label.pack(pady=10)

# Start auto-rotation and application
auto_rotate()
root.mainloop()
