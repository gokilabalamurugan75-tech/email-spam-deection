import tkinter as tk
from tkinter import messagebox
import pickle
import re

# ------------------ Preprocessing Function ------------------
def preprocess_text(text):
    # lowercase
    text = text.lower()
    # remove special characters, numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ------------------ Load Model & Vectorizer ------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ------------------ Prediction Function ------------------
def predict_spam():
    email_text = entry.get("1.0", tk.END).strip()
    if not email_text:
        messagebox.showwarning("Warning", "Please enter an email message!")
        return

    processed_text = preprocess_text(email_text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)

    if prediction[0] == 1:
        messagebox.showinfo("Result", "🚨 This Email is SPAM!")
    else:
        messagebox.showinfo("Result", "✅ This Email is NOT SPAM!")

# ------------------ GUI Design ------------------
root = tk.Tk()
root.title("Email Spam Detector")
root.geometry("500x400")

label = tk.Label(root, text="Enter your email message below:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Text(root, height=10, width=50)
entry.pack(pady=10)

predict_button = tk.Button(root, text="Check Spam", command=predict_spam, bg="blue", fg="white", font=("Arial", 12))
predict_button.pack(pady=10)

root.mainloop()