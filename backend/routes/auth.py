from flask import Blueprint, request, jsonify
from db import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    role = data['role']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s AND role=%s",
                   (username, password, role))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful", "role": role}), 200
    return jsonify({"message": "Invalid credentials"}), 401