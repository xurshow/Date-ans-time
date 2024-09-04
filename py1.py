import tkinter as tk
from datetime import datetime

def update_date():
    now = datetime.now()
    date_label.config(text=f"{now.day}/{now.month}/{now.year}")

root = tk.Tk()
root.title("Date Display")

date_label = tk.Label(root, text="-", font=("Arial", 14), bg="#F0E68C")
date_label.pack()

update_date()

refresh_button = tk.Button(root, text="Refresh", command=update_date)
refresh_button.pack()

root.mainloop()