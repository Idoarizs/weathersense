from flask import Blueprint, request, jsonify

from app.db.models import User

auth_bp = Blueprint(User)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')