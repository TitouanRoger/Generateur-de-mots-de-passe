import tkinter as tk
import string
import random
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Générateur de mots de passe")
        
        self.password_length = tk.IntVar(value=4)
        self.password_strength = tk.StringVar(value="low")
        self.password = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.master, text="Longueur du mot de passe (4-50) :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.length_scale = tk.Scale(self.master, from_=4, to=50, orient="horizontal", variable=self.password_length)
        self.length_scale.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        
        tk.Label(self.master, text="Complexité du mot de passe :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.strength_low = tk.Radiobutton(self.master, text="Faible (chiffres)", variable=self.password_strength, value="low")
        self.strength_low.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.strength_medium = tk.Radiobutton(self.master, text="Moyenne (chiffres et lettres)", variable=self.password_strength, value="medium")
        self.strength_medium.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.strength_high = tk.Radiobutton(self.master, text="Forte (chiffres, lettres, caractères spéciaux)", variable=self.password_strength, value="high")
        self.strength_high.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")
        
        self.generate_button = tk.Button(self.master, text="Générer", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        
        self.copy_button = tk.Button(self.master, text="Copier le mot de passe", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        
        self.password_entry = tk.Entry(self.master, textvariable=self.password, state='readonly')
        self.password_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        
    def generate_password(self):
        length = self.password_length.get()
        strength = self.password_strength.get()
        
        if strength == "low":
            characters = string.digits
        elif strength == "medium":
            characters = string.digits + string.ascii_letters
        elif strength == "high":
            characters = string.digits + string.ascii_letters + string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password.set(password)
        
    def copy_to_clipboard(self):
        pyperclip.copy(self.password.get())

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()