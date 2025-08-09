import tkinter as tk
from tkinter import Canvas, Scrollbar
from datetime import datetime
import re
import random

# Rule-based chatbot function
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey|hii+|heyy)\b", user_input):
        return random.choice([
            "Hello there! How can I assist you today?",
            "Hey! How’s your day going?",
            "Hi! Nice to see you here!"
        ])

    # Farewells
    elif re.search(r"\b(bye|goodbye|see you|exit)\b", user_input):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later! Have a good one!",
            "Bye! Take care!"
        ])

    # How are you
    elif re.search(r"how (are|r) you|hru?|hru", user_input):
        return random.choice([
            "I'm great! how about you?",
            "Doing well, how about you?",
            "Doing awesome, how are you?",
            "I’m fine! How about you?"
        ])

    # Name queries
    elif re.search(r"(your name|who are you)", user_input):
        return "I'm MosBot — your friendly assistant!"

    # Time query
    elif re.search(r"\b(time|current time|what('?s| is) the time|time please)\b", user_input):
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    # Date query
    elif re.search(r"\b(date|today('?s| is) date|what('?s| is) the date|date please)\b", user_input):
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    # Joke
    elif re.search(r"(joke|make me laugh)", user_input):
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I told my computer I needed a break… now it won’t stop sending me Kit-Kats.",
            "Why was the math book sad? It had too many problems."
        ]
        return random.choice(jokes)

    # Math solver (very simple)
    elif re.search(r"^\d+[\+\-\*/]\d+$", user_input):
        try:
            result = eval(user_input)
            return f"The answer is {result}"
        except:
            return "Hmm… that doesn't look like valid math."

    # Default fallback
    else:
        return random.choice([
            "Sorry, I didn’t get that.",
            "Could you rephrase that?",
            "I’m not sure I understand."
        ])

def create_message_bubble(canvas, text, sender="bot"):
    time_str = datetime.now().strftime("%H:%M")
    text_with_time = f"{text}   {time_str}"

    if sender == "user":
        bubble_bg = "#4FC3F7"  # Light blue
        text_color = "black"
        x_start = 380
        anchor_pos = "e"
    else:
        bubble_bg = "#A5D6A7"  # Light green
        text_color = "black"
        x_start = 10
        anchor_pos = "w"

    bubble = canvas.create_text(
        x_start,
        canvas.bbox("all")[3] + 30 if canvas.bbox("all") else 30,
        text=text_with_time,
        font=("Arial", 12),
        fill=text_color,
        width=280,
        anchor=anchor_pos
    )

    coords = canvas.bbox(bubble)
    padding = 10
    rect = canvas.create_rectangle(
        coords[0] - padding, coords[1] - padding,
        coords[2] + padding, coords[3] + padding,
        fill=bubble_bg, outline="", width=0
    )
    canvas.tag_lower(rect, bubble)

    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(1.0)

def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return

    create_message_bubble(chat_canvas, user_input, sender="user")
    entry.delete(0, tk.END)

    bot_reply = chatbot_response(user_input)
    root.after(500, lambda: create_message_bubble(chat_canvas, bot_reply, sender="bot"))


root = tk.Tk()
root.title("MosBot - Smart Rule-Based Chatbot")
root.geometry("420x550")
root.resizable(False, False)
root.configure(bg="#E3F2FD")  # Light blue background

# Header
header = tk.Frame(root, bg="#0288D1", height=50)
header.pack(fill=tk.X)
tk.Label(header, text="MosBot", font=("Arial", 16, "bold"), fg="white", bg="#0288D1").pack(side=tk.LEFT, padx=10)

# Chat area with scrollbar
chat_frame = tk.Frame(root, bg="#E3F2FD")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_canvas = Canvas(chat_frame, bg="#E3F2FD", highlightthickness=0, yscrollcommand=scrollbar.set)
chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=chat_canvas.yview)

# Entry area
entry_frame = tk.Frame(root, bg="#B3E5FC")
entry_frame.pack(fill=tk.X, padx=5, pady=5)

entry = tk.Entry(entry_frame, font=("Arial", 12), bg="white", fg="black", insertbackground="black")
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.bind("<Return>", send_message)  # Press Enter to send

send_btn = tk.Button(entry_frame, text="Send", command=send_message,
                     font=("Arial", 12, "bold"), bg="#0288D1", fg="white", relief="flat")
send_btn.pack(side=tk.RIGHT)

root.mainloop()
