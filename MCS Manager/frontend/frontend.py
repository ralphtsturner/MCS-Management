import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget

class ServerManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft Server Manager")

        self.layout = QVBoxLayout()
        
        self.status_label = QLabel("Welcome to the Server Manager!")
        self.layout.addWidget(self.status_label)
        
        self.server_list_widget = QListWidget()
        self.layout.addWidget(self.server_list_widget)

        self.add_button = QPushButton("Add Server")
        self.add_button.clicked.connect(self.add_server)
        self.layout.addWidget(self.add_button)

        self.start_button = QPushButton("Start Server")
        self.start_button.clicked.connect(self.start_server)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Server")
        self.stop_button.clicked.connect(self.stop_server)
        self.layout.addWidget(self.stop_button)

        self.refresh_servers()
        
        self.setLayout(self.layout)

    def refresh_servers(self):
        """Fetch the list of servers from the backend and update the UI."""
        response = requests.get("http://127.0.0.1:5000/servers/list")
        if response.status_code == 200:
            servers = response.json()
            self.server_list_widget.clear()
            for server in servers:
                self.server_list_widget.addItem(f"{server['name']} - {server['status']}")

    def add_server(self):
        """Add a new server (hardcoded for now)."""
        response = requests.post("http://127.0.0.1:5000/servers/add", json={"name": "MyMinecraftServer", "path": "/path/to/server"})
        if response.status_code == 201:
            self.status_label.setText("Server added successfully!")
            self.refresh_servers()
        else:
            self.status_label.setText("Failed to add server.")

    def start_server(self):
        """Start the selected server."""
        selected_server = self.server_list_widget.currentItem()
        if selected_server:
            server_name = selected_server.text().split(" - ")[0]
            
            response = requests.post(f"http://127.0.0.1:5000/servers/start/{server_name}")
            if response.status_code == 200:
                self.status_label.setText(f"Server '{server_name}' started.")
                self.refresh_servers()
            else:
                self.status_label.setText("Failed to start server.")
        else:
            self.status_label.setText("Please select a server to start.")

    def stop_server(self):
        """Stop the selected server."""
        selected_server = self.server_list_widget.currentItem()
        if selected_server:
            server_name = selected_server.text().split(" - ")[0]
            
            response = requests.post(f"http://127.0.0.1:5000/servers/stop/{server_name}")
            if response.status_code == 200:
                self.status_label.setText(f"Server '{server_name}' stopped.")
                self.refresh_servers()
            else:
                self.status_label.setText("Failed to stop server.")
        else:
            self.status_label.setText("Please select a server to stop.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerManagerApp()
    window.show()
    sys.exit(app.exec_())
