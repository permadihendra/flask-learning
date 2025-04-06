# Database Connection using SQLAlchemy flask_sqlalchemy
# database : sqllite


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///bizza.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
