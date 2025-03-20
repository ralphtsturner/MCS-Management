# db.py
from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'  # your MySQL server address
app.config['MYSQL_USER'] = 'root'       # MySQL username
app.config['MYSQL_PASSWORD'] = 'password'  # MySQL password
app.config['MYSQL_DB'] = 'server_manager'  # Database name

mysql = MySQL(app)
