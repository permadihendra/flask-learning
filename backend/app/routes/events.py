from flask import Blueprint, jsonify, request, current_app
from app.models.event import Event
from app.models import db
import os
from flask_cors import CORS
from datetime import datetime
from werkzeug.exceptions import InternalServerError


events_bp = Blueprint("events", __name__)
CORS(events_bp, origins="http://localhost:3000")
now = datetime.now()


# --------------------------------------
# ROUTE GET EVENTS DATA
# --------------------------------------
@events_bp.route("/", methods=["GET"])
def get_events():
    events = Event.query.all()
    if not events:
        return jsonify({"error": "No events data found"})
    else:
        return jsonify([event.to_dict() for event in events]), 200


# "speaker_id": self.speaker_id,
# "name": self.name,
# "date": self.date,


# --------------------------------------
# ROUTE CREATE EVENTS DATA
# --------------------------------------
@events_bp.route("/", methods=["POST"])
def add_event():
    speaker_id = request.form.get("speaker_id")
    name = request.form.get("name")
    # Convert request form to python datetime
    date = datetime.fromisoformat(request.form.get("date"))

    # Check if data exist
    if not speaker_id or not name or not date:
        return (
            jsonify(
                {
                    "error": "All Fields are required",
                }
            ),
            400,
        )
    else:

        # Querying data if exist in database
        existing_event = Event.query.filter_by(name=name).first()

        if existing_event:
            return jsonify({"error": "Event with that name already exist"}), 409
        else:
            # Execute if record not already exist

            event = Event(
                speaker_id=speaker_id,
                name=name,
                date=date,
            )
            # print(filename)
            db.session.add(event)
            db.session.commit()
            return jsonify(event.to_dict()), 201


# --------------------------------------
# ROUTE UPDATE EVENTS DATA
# --------------------------------------
@events_bp.route("/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    speaker_id = request.form.get("speaker_id")
    name = request.form.get("name")
    # Convert request form to python datetime
    date = datetime.fromisoformat(request.form.get("date"))

    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    elif not all([speaker_id, name, date]):
        return jsonify({"error": "All fields are required"})
    else:
        event.speaker_id = speaker_id
        event.name = name
        event.date = date
        db.session.commit()

        return jsonify({"success": True, "updated speaker": event.to_dict()}), 200


# --------------------------------------
# DELETE  SPEAKER DATA
# --------------------------------------
@events_bp.route("/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = Event.query.get(event_id)
    # if not current_user.has_permission("delete_speaker"):
    #     abort(http.Forbidden("You do not have permission to delete this speaker"))
    # events = Event
    if event:
        db.session.delete(event)
        db.session.commit()
        return (
            jsonify(
                {
                    "success": True,
                    "message": "You deleted a event",
                    "deleted": event.to_dict(),
                }
            ),
            202,
        )
    else:
        return jsonify(message="That event does not exist"), 404
