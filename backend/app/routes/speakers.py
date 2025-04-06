from flask import Blueprint, jsonify, request
from app.models.speaker import Speaker

speakers_bp = Blueprint("speakers", __name__)


@speakers_bp.route("/", methods=["GET"])
def get_speakers():
    speakers = Speaker.query.all()
    if not speakers:
        return jsonify({"error": "No speakers data found"})
    else:
        return jsonify([speaker.serialize() for speaker in speakers]), 200
