import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json

class APITestUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Spring Boot API Tester")
        self.root.geometry("800x600")
        
        # API Base URL
        self.base_url = "http://localhost:8081/api/employees"
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Spring Boot API Tester", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        # GET All Employees Tab
        self.create_get_all_tab(notebook)
        
        # POST Employee Tab
        self.create_post_tab(notebook)
        
        # GET Employee by ID Tab
        self.create_get_by_id_tab(notebook)
        
        # PUT Employee Tab
        self.create_put_tab(notebook)
        
        # DELETE Employee Tab
        self.create_delete_tab(notebook)
        
    def create_get_all_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="GET All Employees")
        
        # Button
        get_btn = tk.Button(frame, text="Get All Employees", command=self.get_all_employees, 
                           bg="#4CAF50", fg="white", font=("Arial", 12))
        get_btn.pack(pady=10)
        
        # Response area
        response_label = tk.Label(frame, text="Response:", font=("Arial", 12, "bold"))
        response_label.pack(pady=5)
        
        self.get_all_response = scrolledtext.ScrolledText(frame, height=15, width=80)
        self.get_all_response.pack(padx=10, pady=5)
        
    def create_post_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="POST Employee")
        
        # Input fields
        input_frame = tk.Frame(frame)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Role:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.role_entry = tk.Entry(input_frame, width=30)
        self.role_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = tk.Entry(input_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Button
        post_btn = tk.Button(frame, text="Create Employee", command=self.post_employee,
                            bg="#2196F3", fg="white", font=("Arial", 12))
        post_btn.pack(pady=10)
        
        # Response area
        response_label = tk.Label(frame, text="Response:", font=("Arial", 12, "bold"))
        response_label.pack(pady=5)
        
        self.post_response = scrolledtext.ScrolledText(frame, height=10, width=80)
        self.post_response.pack(padx=10, pady=5)
        
    def create_get_by_id_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="GET Employee by ID")
        
        # ID input
        id_frame = tk.Frame(frame)
        id_frame.pack(pady=10)
        
        tk.Label(id_frame, text="Employee ID:").pack(side=tk.LEFT, padx=5)
        self.id_entry = tk.Entry(id_frame, width=10)
        self.id_entry.pack(side=tk.LEFT, padx=5)
        
        # Button
        get_id_btn = tk.Button(frame, text="Get Employee", command=self.get_employee_by_id,
                              bg="#FF9800", fg="white", font=("Arial", 12))
        get_id_btn.pack(pady=10)
        
        # Response area
        response_label = tk.Label(frame, text="Response:", font=("Arial", 12, "bold"))
        response_label.pack(pady=5)
        
        self.get_id_response = scrolledtext.ScrolledText(frame, height=10, width=80)
        self.get_id_response.pack(padx=10, pady=5)
        
    def create_put_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="PUT Employee")
        
        # Input fields
        input_frame = tk.Frame(frame)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.put_id_entry = tk.Entry(input_frame, width=10)
        self.put_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.put_name_entry = tk.Entry(input_frame, width=30)
        self.put_name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Role:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.put_role_entry = tk.Entry(input_frame, width=30)
        self.put_role_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.put_email_entry = tk.Entry(input_frame, width=30)
        self.put_email_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Button
        put_btn = tk.Button(frame, text="Update Employee", command=self.put_employee,
                           bg="#9C27B0", fg="white", font=("Arial", 12))
        put_btn.pack(pady=10)
        
        # Response area
        response_label = tk.Label(frame, text="Response:", font=("Arial", 12, "bold"))
        response_label.pack(pady=5)
        
        self.put_response = scrolledtext.ScrolledText(frame, height=10, width=80)
        self.put_response.pack(padx=10, pady=5)
        
    def create_delete_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="DELETE Employee")
        
        # ID input
        id_frame = tk.Frame(frame)
        id_frame.pack(pady=10)
        
        tk.Label(id_frame, text="Employee ID:").pack(side=tk.LEFT, padx=5)
        self.delete_id_entry = tk.Entry(id_frame, width=10)
        self.delete_id_entry.pack(side=tk.LEFT, padx=5)
        
        # Button
        delete_btn = tk.Button(frame, text="Delete Employee", command=self.delete_employee,
                              bg="#F44336", fg="white", font=("Arial", 12))
        delete_btn.pack(pady=10)
        
        # Response area
        response_label = tk.Label(frame, text="Response:", font=("Arial", 12, "bold"))
        response_label.pack(pady=5)
        
        self.delete_response = scrolledtext.ScrolledText(frame, height=10, width=80)
        self.delete_response.pack(padx=10, pady=5)
        
    def get_all_employees(self):
        try:
            response = requests.get(self.base_url)
            self.get_all_response.delete(1.0, tk.END)
            self.get_all_response.insert(tk.END, f"Status Code: {response.status_code}\n")
            self.get_all_response.insert(tk.END, f"Response: {json.dumps(response.json(), indent=2)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get employees: {str(e)}")
            
    def post_employee(self):
        try:
            data = {
                "name": self.name_entry.get(),
                "role": self.role_entry.get(),
                "email": self.email_entry.get()
            }
            
            response = requests.post(self.base_url, json=data, headers={"Content-Type": "application/json"})
            self.post_response.delete(1.0, tk.END)
            self.post_response.insert(tk.END, f"Status Code: {response.status_code}\n")
            self.post_response.insert(tk.END, f"Response: {json.dumps(response.json(), indent=2)}")
            
            # Clear input fields
            self.name_entry.delete(0, tk.END)
            self.role_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create employee: {str(e)}")
            
    def get_employee_by_id(self):
        try:
            employee_id = self.id_entry.get()
            response = requests.get(f"{self.base_url}/{employee_id}")
            self.get_id_response.delete(1.0, tk.END)
            self.get_id_response.insert(tk.END, f"Status Code: {response.status_code}\n")
            self.get_id_response.insert(tk.END, f"Response: {json.dumps(response.json(), indent=2)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get employee: {str(e)}")
            
    def put_employee(self):
        try:
            employee_id = self.put_id_entry.get()
            data = {
                "name": self.put_name_entry.get(),
                "role": self.put_role_entry.get(),
                "email": self.put_email_entry.get()
            }
            
            response = requests.put(f"{self.base_url}/{employee_id}", json=data, headers={"Content-Type": "application/json"})
            self.put_response.delete(1.0, tk.END)
            self.put_response.insert(tk.END, f"Status Code: {response.status_code}\n")
            self.put_response.insert(tk.END, f"Response: {json.dumps(response.json(), indent=2)}")
            
            # Clear input fields
            self.put_id_entry.delete(0, tk.END)
            self.put_name_entry.delete(0, tk.END)
            self.put_role_entry.delete(0, tk.END)
            self.put_email_entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update employee: {str(e)}")
            
    def delete_employee(self):
        try:
            employee_id = self.delete_id_entry.get()
            response = requests.delete(f"{self.base_url}/{employee_id}")
            self.delete_response.delete(1.0, tk.END)
            self.delete_response.insert(tk.END, f"Status Code: {response.status_code}\n")
            if response.status_code == 204:
                self.delete_response.insert(tk.END, "Employee deleted successfully")
            else:
                self.delete_response.insert(tk.END, f"Response: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete employee: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = APITestUI(root)
    root.mainloop() 