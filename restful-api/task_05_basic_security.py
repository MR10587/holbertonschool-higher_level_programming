#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "secret_key"

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def index():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username not in users or password != users.get(username):
        return jsonify({"msg": "Wrong username or password"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@auth.get_user_roles
def get_user_roles(user):
    return user.get_roles()

@app.route('/admin')
@auth.login_required(role='admin')
def admin_entry():
    return f"Hello {auth.current_user()}, you are an admin"

@app.route('/user')
@auth.login_required(role='user')
def user_entry():
    return f"Hello {auth.current_user()}, you are a user"

if __name__ == "__main__":
    app.run()
