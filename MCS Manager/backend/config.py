import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost:3306/db_name?unix_socket=/var/lib/mysql/mysql.sock'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
