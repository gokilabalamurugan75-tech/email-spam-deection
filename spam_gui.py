import tkinter as tk
from tkinter import messagebox
import pickle

# Load model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# GUI window
def detect_spam():
    message = entry.get()
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message.")
        return
    msg_vector = vectorizer.transform([message])
    result = model.predict(msg_vector)[0]
    output = "Spam" if result == 1 else "Not Spam"
    messagebox.showinfo("Result", f"Prediction: {output}")

root = tk.Tk()
root.title("Email Spam Detector")

label = tk.Label(root, text="Enter your message:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Check", command=detect_spam)
button.pack(pady=10)

root.mainloop()