from flask import Flask
from .config import Config
from app.models import db
from app.models.venue import Venue
from app.models.event_registration import EventRegistration

# Import Routes
from app.routes import api


def create_app():
    app = Flask(__name__)

    # Load app configuration from the Config class.
    # using class attributes defined in config.py.
    app.config.from_object(Config)

    # initialize models.db with app
    db.init_app(app)

    # Register Routes API blueprint
    app.register_blueprint(api)

    @app.route("/")
    def index():
        """Return Wellcome message to API home endpoint"""
        return "Welcome to Bizza REST API Server"

    return app
