from flask import Blueprint, request, jsonify
from app.models import db
from app.models.user import User
from werkzeug.exceptions import NotFound, BadRequest
from flask_cors import CORS

users_bp = Blueprint("users", __name__)
CORS(users_bp, origins="http://localhost:3000")


@users_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    if (
        not data
        or not data.get("name")
        or not data.get("email")
        or not data.get("username")
    ):
        raise BadRequest("Username, Name and Email required")

    new_user = User(
        name=data["name"],
        email=data["email"],
        username=data["username"],
        password=data["password"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        role=data["role"],
        is_superuser=data["is_superuser"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"success": True, "user": new_user.to_dict()}), 201


# "username": "john_doe",
#   "name": "John Doe",
#   "email": "john@example.com",
#   "password": "mypassword456",
#   "first_name": "John",
#   "last_name": "Doe",
#   "role": "user",
#   "is_superuser": false


@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200


@users_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if not user:
        raise NotFound("User not found")
    return jsonify(user.to_dict()), 200


@users_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        raise NotFound("User not found")
    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.username = data.get("username", user.username)
    user.password = data.get("password", user.password)
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.role = data.get("role", user.role)
    user.is_superuser = data.get("is_superuser", user.is_superuser)
    db.session.commit()
    return jsonify({"success": True, "user": user.to_dict()}), 200


@users_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        raise NotFound("User not found")
    db.session.delete(user)
    db.session.commit()
    return (
        jsonify({"success": True, "message": "User deleted", "user": user.to_dict()}),
        200,
    )
