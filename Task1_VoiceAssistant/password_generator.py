"""
Task 4 - Random Password Generator
Oasis Infobyte Python Programming Internship

A Tkinter-based GUI application that generates strong, random passwords
based on user-selected criteria (length, uppercase, lowercase, digits,
symbols). Includes a "copy to clipboard" feature and a simple strength
indicator.

Author: Anupam Ram Tripathi
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator - OASIS Infobyte")
        self.root.geometry("420x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self._build_ui()

    # ---------- UI SETUP ----------
    def _build_ui(self):
        title_label = tk.Label(
            self.root,
            text="🔐 Random Password Generator",
            font=("Helvetica", 16, "bold"),
            bg="#1e1e2f",
            fg="#ffffff",
        )
        title_label.pack(pady=20)

        # Password length
        length_frame = tk.Frame(self.root, bg="#1e1e2f")
        length_frame.pack(pady=10)

        tk.Label(
            length_frame,
            text="Password Length:",
            font=("Helvetica", 11),
            bg="#1e1e2f",
            fg="#ffffff",
        ).grid(row=0, column=0, padx=5)

        self.length_var = tk.IntVar(value=12)
        self.length_spin = tk.Spinbox(
            length_frame,
            from_=4,
            to=64,
            textvariable=self.length_var,
            width=5,
            font=("Helvetica", 11),
            justify="center",
        )
        self.length_spin.grid(row=0, column=1, padx=5)

        # Character set options
        options_frame = tk.LabelFrame(
            self.root,
            text="Include Character Types",
            font=("Helvetica", 11, "bold"),
            bg="#1e1e2f",
            fg="#ffffff",
            labelanchor="n",
            padx=15,
            pady=10,
        )
        options_frame.pack(pady=15, padx=30, fill="x")

        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        style_kwargs = dict(
            bg="#1e1e2f",
            fg="#ffffff",
            selectcolor="#2e2e42",
            font=("Helvetica", 10),
            activebackground="#1e1e2f",
            activeforeground="#ffffff",
        )

        tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.use_upper, **style_kwargs).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.use_lower, **style_kwargs).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.use_digits, **style_kwargs).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Symbols (!@#$%)", variable=self.use_symbols, **style_kwargs).pack(anchor="w")

        # Generate button
        generate_btn = tk.Button(
            self.root,
            text="Generate Password",
            font=("Helvetica", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#43a047",
            relief="flat",
            padx=10,
            pady=8,
            command=self.generate_password,
        )
        generate_btn.pack(pady=15)

        # Output field
        self.password_var = tk.StringVar()
        output_entry = tk.Entry(
            self.root,
            textvariable=self.password_var,
            font=("Consolas", 13),
            justify="center",
            width=28,
            bd=2,
            relief="solid",
        )
        output_entry.pack(pady=5)

        # Copy button
        copy_btn = tk.Button(
            self.root,
            text="📋 Copy to Clipboard",
            font=("Helvetica", 10),
            bg="#2196F3",
            fg="white",
            relief="flat",
            padx=8,
            pady=5,
            command=self.copy_to_clipboard,
        )
        copy_btn.pack(pady=10)

        # Strength indicator
        self.strength_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 11, "bold"),
            bg="#1e1e2f",
        )
        self.strength_label.pack(pady=10)

        footer = tk.Label(
            self.root,
            text="OASIS Infobyte | Python Internship - Task 4",
            font=("Helvetica", 8),
            bg="#1e1e2f",
            fg="#888888",
        )
        footer.pack(side="bottom", pady=10)

    # ---------- LOGIC ----------
    def generate_password(self):
        length = self.length_var.get()

        char_pool = ""
        if self.use_upper.get():
            char_pool += string.ascii_uppercase
        if self.use_lower.get():
            char_pool += string.ascii_lowercase
        if self.use_digits.get():
            char_pool += string.digits
        if self.use_symbols.get():
            char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if not char_pool:
            messagebox.showwarning(
                "No character type selected",
                "Please select at least one character type to generate a password.",
            )
            return

        password = "".join(random.choice(char_pool) for _ in range(length))
        self.password_var.set(password)
        self._update_strength(password)

    def _update_strength(self, password):
        length = len(password)
        variety = sum(
            [
                any(c.isupper() for c in password),
                any(c.islower() for c in password),
                any(c.isdigit() for c in password),
                any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
            ]
        )

        if length >= 12 and variety >= 3:
            self.strength_label.config(text="Strength: Strong ✅", fg="#4CAF50")
        elif length >= 8 and variety >= 2:
            self.strength_label.config(text="Strength: Medium ⚠️", fg="#FFC107")
        else:
            self.strength_label.config(text="Strength: Weak ❌", fg="#F44336")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if not password:
            messagebox.showinfo("Nothing to Copy", "Generate a password first!")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
