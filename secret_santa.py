import tkinter as tk
from tkinter import ttk
import random
from playsound import playsound
import threading

# ✅ Voeg hier die name van almal wat deelneem
participants = [
    "Jacqueline", "Shane", "Klea", "Leshe", "Lynnette", "Diederick", "Katie", "David", "Kiana", "Antonie", "Bella", "Rene", "Ouma"
]

# Maak toewysings (geen self-pairing)
def generate_assignments(names):
    while True:
        shuffled = names[:]
        random.shuffle(shuffled)
        if all(a != b for a, b in zip(names, shuffled)):
            return dict(zip(names, shuffled))

assignments = generate_assignments(participants)

# Wishlist dictionary
wishlist = {}

# Stoor wishlist na lêer
def save_wishlist():
    with open("wishlist.txt", "w", encoding="utf-8") as f:
        for name, ideas in wishlist.items():
            f.write(f"{name}: {', '.join(ideas)}\n")

# Speel Jingle Bells in agtergrond
def play_jingle():
    threading.Thread(target=lambda: playsound(r"C:\\Users\\knoes\\Desktop\\jingle_bells.mp3.mp3"), daemon=True).start()

# Wys Secret Santa en wishlist van ontvanger
def submit_info():
    name = name_entry.get().strip()
    if name in assignments:
        recipient = assignments[name]
        # Kry idees van huidige gebruiker
        ideas = [e.get().strip() for e in idea_entries if e.get().strip()]
        wishlist[name] = ideas
        save_wishlist()
        # Kry wishlist van ontvanger
        recipient_ideas = wishlist.get(recipient, [])
        if recipient_ideas:
            wishlist_text = f"Hul wishlist: {', '.join(recipient_ideas)}"
        else:
            wishlist_text = "Geen wishlist beskikbaar nie."
        result_label.config(text=f"🎄 Jy moet koop vir: {recipient}\n{wishlist_text}", foreground="#004d40")
        play_jingle()
    else:
        result_label.config(text="❌ Naam nie gevind nie! Maak seker jy is op die lys.", foreground="red")

# Admin sien alle wishlists
def view_wishlist():
    if not wishlist:
        result_label.config(text="Geen wishlist data beskikbaar nie.", foreground="orange")
    else:
        all_data = "\n".join([f"{name}: {', '.join(ideas)}" for name, ideas in wishlist.items()])
        result_label.config(text=f"Alle Wishlists:\n{all_data}", foreground="#004d40")

# GUI
root = tk.Tk()
root.title("Secret Santa - Christmas Carols Edition")
root.geometry("550x600")
root.configure(bg="#FF6666")

style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 18, "bold"), padding=10)
style.configure("TLabel", background="#FF6666", foreground="white", font=("Comic Sans MS", 16))

# Titel
title_label = ttk.Label(root, text="🎶 Ons Christmas Carols Secret Santa 🎶", font=("Comic Sans MS", 25, "bold"))
title_label.pack(pady=15)

# Naam invoer
name_label = ttk.Label(root, text="Voer jou naam in:")
name_label.pack()
name_entry = ttk.Entry(root, font=("Helvetica", 14))
name_entry.pack(pady=10)

# Geskenk idees
idea_entries = []
for i in range(3):
    lbl = ttk.Label(root, text=f"Geskenk idee {i+1}:")
    lbl.pack()
    entry = ttk.Entry(root, font=("Comic Sans MS", 14))
    entry.pack(pady=3)
    idea_entries.append(entry)

# Resultaat label
result_label = ttk.Label(root, text="", font=("Comic Sans MS", 14, "bold"))
result_label.pack(pady=20)

# Knoppies
submit_button = ttk.Button(root, text="Bevestig en Kry My Secret Santa", command=submit_info)
submit_button.pack(pady=10)

admin_button = ttk.Button(root, text="Admin: Sien Alle Wishlists", command=view_wishlist)
admin_button.pack(pady=10)

footer_label = ttk.Label(root, text="Ho Ho Ho! 🎁 Sing saam met die kersliedere!", font=("Helvetica", 12, "italic"))
footer_label.pack(side="bottom", pady=10)

root.mainloop()