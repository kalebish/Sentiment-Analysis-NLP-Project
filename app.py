import tkinter as tk
from tkinter import messagebox
import pickle

with open('model.pkl', 'rb') as model_file, open('vectorizer.pkl', 'rb') as vect_file:
    model = pickle.load(model_file)
    vect = pickle.load(vect_file)


root = tk.Tk()
root.title("Sentiment Analysis")
root.geometry("400x300")

def analyze_sentiment():
    review = text_entry.get("1.0", tk.END).strip()
    if review:
        review_vectorized = vect.transform([review])
        discrete = model.predict(review_vectorized)
        prob = model.predict_proba(review_vectorized)[0][1]
        result = f"Probability of being positive: {prob:.4f}"
        result_label.config(text=result)

        if discrete:
            positive_light_canvas.itemconfig(positive_light_oval, fill='green')
            negative_light_canvas.itemconfig(negative_light_oval, fill='gray')
        else:
            positive_light_canvas.itemconfig(positive_light_oval, fill='gray')
            negative_light_canvas.itemconfig(negative_light_oval, fill='red')
    else:
        messagebox.showwarning("Input Error", "Please enter a review to analyze.")




title_label = tk.Label(root, text="Sentiment Analysis", font=("Helvetica", 16))
title_label.pack(pady=10)

title_label = tk.Label(root, text="Your Message", font=("Helvetica", 16))
text_entry = tk.Text(root, height=10, width=40, )
text_entry.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)


lights_frame = tk.Frame(root)
lights_frame.pack(pady=10)

positive_label = tk.Label(lights_frame, text="Positive", font=("Helvetica", 12))
positive_label.grid(row=0, column=0, padx=10)

positive_light_canvas = tk.Canvas(lights_frame, width=20, height=20)
positive_light_oval = positive_light_canvas.create_oval(5, 5, 15, 15, fill='gray')
positive_light_canvas.grid(row=0, column=1)

negative_label = tk.Label(lights_frame, text="Negative", font=("Helvetica", 12))
negative_label.grid(row=0, column=2, padx=10)

negative_light_canvas = tk.Canvas(lights_frame, width=20, height=20)
negative_light_oval = negative_light_canvas.create_oval(5, 5, 15, 15, fill='gray')
negative_light_canvas.grid(row=0, column=3)

analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=10)



root.mainloop()