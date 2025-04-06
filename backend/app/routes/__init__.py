from flask import Blueprint

# Import routes bluprints
from app.routes.speakers import speakers_bp
from app.routes.venues import venues_bp
from app.routes.registrations import registrations_bp

# Shared blueprint for all route modules
api = Blueprint("api", __name__)

api.register_blueprint(speakers_bp, url_prefix="/api/v1/speakers")
api.register_blueprint(venues_bp)
api.register_blueprint(registrations_bp)
