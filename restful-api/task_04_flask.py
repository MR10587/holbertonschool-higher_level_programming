#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data/<variable_name>')
def data(variable_name):
    return jsonify(variable_name)

@app.route('/status')
def start():
    return "OK"

@app.route('/users/<username>')
def user(username):
    try:
        return escape(username)
    except Exception:
        return jsonify("400 error:Invalid JSON")

@app.route('/add_user/<username>', methods=['GET', 'POST'])
def login(data):
    if request.method == 'POST':
        if username:
            return jsonify("409 error:Username already exists")
        try:
            text = request.get_json(data)
            username = text['username']
            return f"User {username} added"
        except json.JSONDecodeError:
            return jsonify("400 error:Invalid JSON")
        if not username:
            return jsonify("400 error:Username is required")
        



if __name__ == "__main__": 
    app.run()