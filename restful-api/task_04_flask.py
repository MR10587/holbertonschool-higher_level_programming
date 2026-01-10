#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return 'OK'

@app.route('/users/<username>')
def account(username):
    if not username in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route('/add_user', methods=['POST'])
def new_user():
    data = request.to_json()
    if data is None:
        return jsonify({"error":"Invalid JSON"}), 400
    if not username:
        return jsonify({"error":"Username is required"}), 400
    if username in users:
        return jsonify({"error":"Username already exists"}), 409

    users[username] = data
    return 'User added'

if __name__ == "__main__":
    app.run()