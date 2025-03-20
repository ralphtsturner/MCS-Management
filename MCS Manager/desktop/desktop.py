# desktop.py
import tkinter as tk
from tkinter import messagebox
import requests

class ServerManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Server Manager")
        
        # Listbox to display servers
        self.server_listbox = tk.Listbox(self.root, width=50, height=15)
        self.server_listbox.pack(pady=20)
        
        # Add Server Button
        self.add_server_button = tk.Button(self.root, text="Add Server", command=self.add_server)
        self.add_server_button.pack(pady=10)
        
        self.load_servers()
    
    def load_servers(self):
        response = requests.get('http://localhost:5000/servers')  # Assuming Flask is running on localhost
        if response.status_code == 200:
            servers = response.json()
            for server in servers:
                self.server_listbox.insert(tk.END, f"Name: {server['name']} | IP: {server['ip']} | Status: {server['status']}")
    
    def add_server(self):
        name = simpledialog.askstring("Server Name", "Enter server name:")
        ip = simpledialog.askstring("IP Address", "Enter server IP:")
        status = simpledialog.askstring("Status", "Enter server status:")
        # Add server via Flask route
        response = requests.post('http://localhost:5000/add_server', data={'name': name, 'ip': ip, 'status': status})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Server added successfully!")
            self.load_servers()
        else:
            messagebox.showerror("Error", "Failed to add server.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerManagerApp(root)
    root.mainloop()
