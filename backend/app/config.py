# Database Connection using SQLAlchemy flask_sqlalchemy
# database : sqllite
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///bizza.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "public", "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
