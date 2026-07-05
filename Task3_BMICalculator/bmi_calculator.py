"""
BMI Calculator - OASIS INFOBYTE Internship (Task 3)
Author: Anupam Tripathi

A simple GUI-based BMI (Body Mass Index) Calculator using Tkinter.
Enter your weight (kg) and height (cm or m) to calculate your BMI
and see which health category you fall into.

Install dependency (none extra needed, Tkinter comes built-in with Python):
    (No pip install required)
"""

import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showwarning(
                "Invalid Input", "Weight and height must be positive numbers."
            )
            return

        height_m = height_cm / 100  # convert cm to meters
        bmi = weight / (height_m ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"  # blue
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            color = "#2ecc71"  # green
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "#f39c12"  # orange
        else:
            category = "Obese"
            color = "#e74c3c"  # red

        bmi_value_label.config(text=f"Your BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}", fg=color)

    except ValueError:
        messagebox.showwarning(
            "Invalid Input", "Please enter valid numeric values for weight and height."
        )


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_value_label.config(text="")
    category_label.config(text="")


# ------------------ GUI SETUP ------------------
root = tk.Tk()
root.title("BMI Calculator - OASIS INFOBYTE")
root.geometry("400x480")
root.resizable(False, False)
root.configure(bg="#1e3d59")

heading = tk.Label(
    root, text="⚖ BMI Calculator", font=("Segoe UI", 20, "bold"),
    bg="#1e3d59", fg="white"
)
heading.pack(pady=20)

form_frame = tk.Frame(root, bg="#1e3d59")
form_frame.pack(pady=10)

# Weight input
weight_label = tk.Label(
    form_frame, text="Weight (kg):", font=("Segoe UI", 12), bg="#1e3d59", fg="white"
)
weight_label.grid(row=0, column=0, sticky="w", pady=8, padx=5)

weight_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=15, justify="center")
weight_entry.grid(row=0, column=1, pady=8, padx=5)

# Height input
height_label = tk.Label(
    form_frame, text="Height (cm):", font=("Segoe UI", 12), bg="#1e3d59", fg="white"
)
height_label.grid(row=1, column=0, sticky="w", pady=8, padx=5)

height_entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=15, justify="center")
height_entry.grid(row=1, column=1, pady=8, padx=5)

# Buttons
button_frame = tk.Frame(root, bg="#1e3d59")
button_frame.pack(pady=15)

calculate_btn = tk.Button(
    button_frame, text="Calculate BMI", font=("Segoe UI", 11, "bold"),
    bg="#ff6e40", fg="white", command=calculate_bmi, cursor="hand2", width=14
)
calculate_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(
    button_frame, text="Clear", font=("Segoe UI", 11, "bold"),
    bg="#607d8b", fg="white", command=clear_fields, cursor="hand2", width=10
)
clear_btn.grid(row=0, column=1, padx=5)

# Result section
result_frame = tk.Frame(root, bg="#1e3d59")
result_frame.pack(pady=25)

bmi_value_label = tk.Label(
    result_frame, text="", font=("Segoe UI", 16, "bold"), bg="#1e3d59", fg="#ffc13b"
)
bmi_value_label.pack(pady=5)

category_label = tk.Label(
    result_frame, text="", font=("Segoe UI", 13, "bold"), bg="#1e3d59"
)
category_label.pack(pady=5)

# BMI scale reference
scale_frame = tk.Frame(root, bg="#1e3d59")
scale_frame.pack(pady=10)

scale_text = (
    "BMI Scale:\n"
    "Below 18.5      -> Underweight\n"
    "18.5 - 24.9     -> Normal weight\n"
    "25.0 - 29.9     -> Overweight\n"
    "30.0 and above  -> Obese"
)
scale_label = tk.Label(
    scale_frame, text=scale_text, font=("Consolas", 9), bg="#1e3d59",
    fg="#9fb3c8", justify="left"
)
scale_label.pack()

footer = tk.Label(
    root, text="OASIS INFOBYTE Internship - Task 3",
    font=("Segoe UI", 9), bg="#1e3d59", fg="#9fb3c8"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
