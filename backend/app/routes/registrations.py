from flask import Blueprint, jsonify, request
from app.models.event_registration import EventRegistration
from app.models import db


registrations_bp = Blueprint("registrations", __name__)


@registrations_bp.route("/api/v1/events-registration", methods=["POST"])
def add_attendees():
    if request.method == "POST":
        data = request.get_json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone = data.get("phone")
        job_title = data.get("job_title")
        company_name = data.get("company_name")
        company_size = data.get("company_size")
        subject = data.get("subject")

        print(data)

        if first_name and last_name and email and phone and subject:
            existing_attendee = EventRegistration.query.filter_by(email=email).first()

            if existing_attendee:
                return jsonify(message="Email address already exists!"), 409
            else:
                new_attendee = EventRegistration(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    job_title=job_title,
                    company_name=company_name,
                    company_size=company_size,
                    subject=subject,
                )
                db.session.add(new_attendee)
                db.session.commit()

                return (
                    jsonify({"success": True, "new_attendee": new_attendee.format()}),
                    201,
                )
        else:
            return jsonify({"error": "Invalid input"}), 400


# Event Registration -> view all registration
@registrations_bp.route("/api/v1/events-registration", methods=["GET"])
def retrieve_attendees():
    if request.method == "GET":
        all_attendees = EventRegistration.query.all()
        if all_attendees:
            return (
                jsonify(
                    {
                        "success": True,
                        "venues": [attendees.format() for attendees in all_attendees],
                    }
                ),
                200,
            )
        else:
            return jsonify(message="No venue record found!"), 404
