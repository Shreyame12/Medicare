
import re

from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


def get_request_data():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return None

    return data


def valid_email(email):
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return bool(re.fullmatch(pattern, email))


@auth_bp.route("/register", methods=["POST"])
def register():
    data = get_request_data()

    if data is None:
        return jsonify({
            "status": "error",
            "message": "A valid JSON object is required"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not all(isinstance(value, str) for value in [name, email, password]):
        return jsonify({
            "status": "error",
            "message": "Name, email and password are required"
        }), 400

    name = name.strip()
    email = email.strip().lower()

    if not name or not email or not password:
        return jsonify({
            "status": "error",
            "message": "Name, email and password are required"
        }), 400

    if not valid_email(email):
        return jsonify({
            "status": "error",
            "message": "Please provide a valid email address"
        }), 400

    if len(password) < 8:
        return jsonify({
            "status": "error",
            "message": "Password must be at least 8 characters"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Registration details validated"
    }), 200


@auth_bp.route("/login", methods=["POST"])
def login():
    data = get_request_data()

    if data is None:
        return jsonify({
            "status": "error",
            "message": "A valid JSON object is required"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not isinstance(email, str) or not isinstance(password, str):
        return jsonify({
            "status": "error",
            "message": "Email and password are required"
        }), 400

    email = email.strip().lower()

    if not email or not password:
        return jsonify({
            "status": "error",
            "message": "Email and password are required"
        }), 400

    if not valid_email(email):
        return jsonify({
            "status": "error",
            "message": "Please provide a valid email address"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Login details received"
    }), 200
