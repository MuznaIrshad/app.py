import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# File to store attendance data
FILE_NAME = "attendance.xlsx"

def save_attendance():
    name = name_entry.get()
    roll = roll_entry.get()
    status = status_var.get()
    
    if not name or not roll or status not in ["Present", "Absent"]:
        messagebox.showerror("Error", "Please enter all fields correctly!")
        return
    
    # Check if file exists
    if os.path.exists(FILE_NAME):
        df = pd.read_excel(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Name", "Roll Number", "Status"])
    
    # Append new data
    new_data = pd.DataFrame([[name, roll, status]], columns=["Name", "Roll Number", "Status"])
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Save to Excel
    df.to_excel(FILE_NAME, index=False)
    messagebox.showinfo("Success", "Attendance marked successfully!")
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Attendance App")
root.geometry("300x250")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number:").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

status_var = tk.StringVar()
tk.Label(root, text="Status:").pack()
tk.Radiobutton(root, text="Present", variable=status_var, value="Present").pack()
tk.Radiobutton(root, text="Absent", variable=status_var, value="Absent").pack()

tk.Button(root, text="Save Attendance", command=save_attendance).pack()

root.mainloop()
