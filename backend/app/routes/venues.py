from flask import Blueprint, jsonify, request
from app.models.venue import Venue
from app.models import db

venues_bp = Blueprint("venues", __name__)


# Venues API Endpont -> add new venue
@venues_bp.route("/api/v1/venues", methods=["POST"])
def add_venues():
    if request.method == "POST":
        name = request.get_json().get("name")
        all_venues = Venue.query.filter_by(name=name).first()
        if all_venues:
            return jsonify(message="Venue name already exist!"), 409
        else:
            new_venue = Venue(name=name)
            db.session.add(new_venue)
            db.session.commit()
            return jsonify({"success": True, "venues": new_venue.format()}), 201


# Venues API endpoint -> retrieve all the venues in database
@venues_bp.route("/api/v1/venues", methods=["GET"])
def retrieve_venues():
    if request.method == "GET":
        all_venues = Venue.query.all()
        if all_venues:
            return (
                jsonify(
                    {
                        "success": True,
                        "venues": [venue.format() for venue in all_venues],
                    }
                ),
                200,
            )
        else:
            return jsonify(message="No venue record found!"), 404


# Venues API Endpoint --> return single venue
@venues_bp.route("/api/v1/venues/<int:id>", methods=["GET"])
def retrieve_venue(id):
    if request.method == "GET":
        venue = Venue.query.filter(Venue.id == id).first()
        if venue:
            return jsonify({"success": True, "venue": venue.format()}), 200
        else:
            return jsonify(message="Record id not found"), 404


# Venues API Endpoint --> update single venue record
@venues_bp.route("/api/v1/venues/<int:id>", methods=["PUT"])
def update_venue(id):
    if request.method == "PUT":
        name = request.get_json().get("name")
        venue = Venue.query.get(id)
        if not venue:
            return jsonify(message="Venue record not found"), 404
        else:
            venue.name = name
            db.session.commit()
            return jsonify({"success": True, "updated venue": venue.format()}), 200


# Venues API Endpoint --> delete single venue record
@venues_bp.route("/api/v1/venues/<int:id>", methods=["DELETE"])
def remove_venue(id):
    if request.method == "DELETE":
        venue = Venue.query.filter(Venue.id == id).first()
        if venue:
            db.session.delete(venue)
            db.session.commit()
            return (
                jsonify(
                    {
                        "success": True,
                        "message": "You deleted a venue",
                        "deleted": venue.format(),
                    }
                ),
                202,
            )
        else:
            return jsonify(message="That venue does not exist"), 404
