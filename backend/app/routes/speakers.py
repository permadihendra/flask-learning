from flask import Blueprint, jsonify, request, current_app
from app.models.speaker import Speaker
from app.models import db
import os, re
from flask_cors import CORS
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.exceptions import InternalServerError


speakers_bp = Blueprint("speakers", __name__)
CORS(speakers_bp, origins="http://localhost:3000")
now = datetime.now()


# --------------------------------------
# ROUTE GET SPEAKER DATA
# --------------------------------------
@speakers_bp.route("/", methods=["GET"])
def get_speakers():
    speakers = Speaker.query.all()
    if not speakers:
        return jsonify({"error": "No speakers data found"})
    else:
        return jsonify([speaker.serialize() for speaker in speakers]), 200


# --------------------------------------
# ROUTE CREATE SPEAKER DATA
# --------------------------------------
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
            filename = secure_filename(email + "_" + avatar.filename)
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


# # Function to check secure filename
# def secure_filename(filename, email):
#     new_filename = email + "_" + filename
#     filename = os.path.basename(filename)  # Remove directory path
#     filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", new_filename)  # Replace unsafe chars
#     return filename


# --------------------------------------
# ROUTE UPDATE SPEAKER DATA
# --------------------------------------
@speakers_bp.route("/<int:speaker_id>", methods=["PUT"])
def update_speaker(speaker_id):
    name = request.form.get("name")
    email = request.form.get("email")
    company = request.form.get("company")
    position = request.form.get("position")
    bio = request.form.get("bio")
    avatar = request.files.get("speaker_avatar")

    speaker = Speaker.query.get(speaker_id)
    if not speaker:
        return jsonify({"error": "Speaker not found"}), 404
    elif not all([name, email, company, position, bio]):
        return jsonify({"error": "All fields are required"})
    elif email != speaker.email:
        return jsonify(message="Can not change existing email"), 401
    else:
        speaker.name = name
        speaker.email = email
        speaker.company = company
        speaker.position = position
        speaker.bio = bio
        db.session.commit()

        # next check upload avatar
        if avatar and allowed_file(avatar.filename):
            filename = secure_filename(email + "_" + avatar.filename)
            # save avatar images
            avatar.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            print(avatar)

        return jsonify({"success": True, "updated speaker": speaker.format()}), 200


# --------------------------------------
# DELETE UPDATE SPEAKER DATA
# --------------------------------------
@speakers_bp.route("/<int:speaker_id>", methods=["DELETE"])
def delete_speaker(speaker_id):
    speaker = Speaker.query.get(speaker_id)
    # if not current_user.has_permission("delete_speaker"):
    #     abort(http.Forbidden("You do not have permission to delete this speaker"))
    # events = Event
    if speaker:
        db.session.delete(speaker)
        db.session.commit()
        return (
            jsonify(
                {
                    "success": True,
                    "message": "You deleted a speaker",
                    "deleted": speaker.format(),
                }
            ),
            202,
        )
    else:
        return jsonify(message="That speaker does not exist"), 404
