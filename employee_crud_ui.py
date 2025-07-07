import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

API_URL = "http://localhost:8080/api/employees"

def refresh_list():
    listbox.delete(0, tk.END)
    try:
        resp = requests.get(API_URL)
        resp.raise_for_status()
        for emp in resp.json():
            listbox.insert(tk.END, f"{emp['id']}: {emp['name']}, {emp['role']}, {emp['email']}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_employee():
    name = simpledialog.askstring("Input", "Name:")
    role = simpledialog.askstring("Input", "Role:")
    email = simpledialog.askstring("Input", "Email:")
    if name and role and email:
        try:
            resp = requests.post(API_URL, json={"name": name, "role": role, "email": email})
            resp.raise_for_status()
            refresh_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def delete_employee():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return
    emp_id = selected.split(":")[0]
    try:
        resp = requests.delete(f"{API_URL}/{emp_id}")
        resp.raise_for_status()
        refresh_list()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_employee():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return
    emp_id = selected.split(":")[0]
    name = simpledialog.askstring("Input", "New Name:")
    role = simpledialog.askstring("Input", "New Role:")
    email = simpledialog.askstring("Input", "New Email:")
    if name and role and email:
        try:
            resp = requests.put(f"{API_URL}/{emp_id}", json={"name": name, "role": role, "email": email})
            resp.raise_for_status()
            refresh_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Employee CRUD UI")

listbox = tk.Listbox(root, width=60)
listbox.pack()

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Refresh", command=refresh_list).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Add", command=add_employee).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Update", command=update_employee).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Delete", command=delete_employee).pack(side=tk.LEFT)

refresh_list()
root.mainloop() 