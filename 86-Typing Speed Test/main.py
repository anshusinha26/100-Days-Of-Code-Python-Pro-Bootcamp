import tkinter as tk
import time
import random

# Sample texts for typing test
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a popular programming language.",
    "Typing speed tests are a fun way to improve your accuracy.",
    "Consistency is key when learning new skills.",
    "Focus on accuracy first, speed will follow."
]


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Sample text selection
        self.sample_text = random.choice(sample_texts)

        # Variables for tracking typing time and input
        self.start_time = None
        self.input_text = tk.StringVar()

        # UI elements
        self.create_widgets()

    def create_widgets(self):
        # Display the sample text
        tk.Label(
            self.root, text="Type the following text:",
            font=("Arial", 14), bg="#000"
        ).pack(pady=10)

        self.sample_text_label = tk.Label(
            self.root, text=self.sample_text,
            font=("Arial", 16), wraplength=550, justify="center", bg="#000",
            relief="solid", padx=10, pady=10
        )
        self.sample_text_label.pack(pady=10)

        # Entry box for typing input
        self.entry = tk.Entry(
            self.root, textvariable=self.input_text,
            font=("Arial", 14), width=50
        )
        self.entry.pack(pady=20)
        self.entry.bind("<FocusIn>", self.start_typing)
        self.entry.bind("<Return>", self.calculate_speed)

        # Button to finish and calculate speed
        tk.Button(
            self.root, text="Finish", command=self.calculate_speed,
            font=("Arial", 12), bg="#fff", fg="black", relief="raised"
        ).pack(pady=20)

        # Label for displaying typing speed feedback
        self.result_label = tk.Label(self.root, font=("Arial", 14), bg="#000")
        self.result_label.pack(pady=10)

    def start_typing(self, event):
        if self.start_time is None:  # Only set the start time on the first keystroke
            self.start_time = time.time()

    def calculate_speed(self, event=None):
        if self.start_time is None:
            return  # Prevent calculating speed if typing hasn't started

        # Calculate typing duration and speed
        end_time = time.time()
        typing_duration = end_time - self.start_time
        words_typed = len(self.input_text.get().split())
        words_per_minute = (words_typed / typing_duration) * 60

        # Accuracy calculation
        correct_words = sum(
            1 for i, word in enumerate(self.input_text.get().split())
            if i < len(self.sample_text.split()) and word == self.sample_text.split()[i]
        )
        accuracy = (correct_words / len(self.sample_text.split())) * 100

        # Display results
        self.result_label.config(
            text=f"Typing Speed: {words_per_minute:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        )
        self.start_time = None  # Reset start time for next test


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
