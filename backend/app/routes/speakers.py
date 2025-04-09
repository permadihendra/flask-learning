from flask import Blueprint, jsonify, request, current_app
from app.models.speaker import Speaker
from app.models import db
import os, re
from flask_cors import CORS
from datetime import datetime


speakers_bp = Blueprint("speakers", __name__)
CORS(speakers_bp, origins="http://localhost:3000")
now = datetime.now()


@speakers_bp.route("/", methods=["GET"])
def get_speakers():
    speakers = Speaker.query.all()
    if not speakers:
        return jsonify({"error": "No speakers data found"})
    else:
        return jsonify([speaker.serialize() for speaker in speakers]), 200


@speakers_bp.route("/", methods=["POST"])
def add_speaker():
    name = request.form.get("name")
    email = request.form.get("email")
    company = request.form.get("company")
    position = request.form.get("position")
    bio = request.form.get("bio")
    # avatar_name = request.form.get("avatar_name")
    avatar = request.files.get("speaker_avatar")  # for file input

    # print(current_app.config["UPLOAD_FOLDER"])

    # Check if data exist
    if not name or not email or not company or not position or not bio:
        return (
            jsonify(
                {
                    "error": "All Fields are required",
                }
            ),
            400,
        )
    else:
        # next check upload avatar
        if avatar and allowed_file(avatar.filename):
            filename = secure_filename(avatar.filename, email)
        else:
            filename = "default-avatar.jpg"

    # Querying data if exist in database
    existing_speaker = Speaker.query.filter_by(email=email).first()

    if existing_speaker:
        return jsonify({"error": "Sepaker with that email already exist"}), 409
    else:
        # Execute if record not already exist
        # save avatar images
        avatar.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))

        speaker = Speaker(
            name=name,
            email=email,
            company=company,
            position=position,
            bio=bio,
            speaker_avatar=filename,
        )
        # print(filename)
        db.session.add(speaker)
        db.session.commit()
        return jsonify(speaker.serialize()), 201


# Function to check if the file extension is allowed
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


# Function to check secure filename
def secure_filename(filename, email):
    new_filename = email + "_" + filename
    filename = os.path.basename(filename)  # Remove directory path
    filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", new_filename)  # Replace unsafe chars
    return filename
