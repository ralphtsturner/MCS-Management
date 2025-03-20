# models.py
from db import mysql

class Server:
    @staticmethod
    def get_all_servers():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM servers")
        servers = cur.fetchall()
        cur.close()
        return servers

    @staticmethod
    def add_server(name, ip, status):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO servers (name, ip, status) VALUES (%s, %s, %s)", (name, ip, status))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete_server(server_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM servers WHERE id = %s", (server_id,))
        mysql.connection.commit()
        cur.close()
