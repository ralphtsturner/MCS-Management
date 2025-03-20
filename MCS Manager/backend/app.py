# app.py
from flask import Flask, jsonify, request
from server_routes import *
from db import app

if __name__ == "__main__":
    app.run(debug=True)
