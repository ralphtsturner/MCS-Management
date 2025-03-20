# server_routes.py
from flask import render_template, request, redirect, url_for
from models import Server
from app import app

@app.route('/servers')
def show_servers():
    servers = Server.get_all_servers()
    return render_template('servers.html', servers=servers)

@app.route('/add_server', methods=['POST'])
def add_server():
    if request.method == 'POST':
        name = request.form['name']
        ip = request.form['ip']
        status = request.form['status']
        Server.add_server(name, ip, status)
        return redirect(url_for('show_servers'))

@app.route('/delete_server/<int:server_id>', methods=['GET'])
def delete_server(server_id):
    Server.delete_server(server_id)
    return redirect(url_for('show_servers'))
