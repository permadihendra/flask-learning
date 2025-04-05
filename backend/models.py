from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Database Connection using SQLAlchemy flask_sqlalchemy
# database : sqllite

# define db sqlalchemy
db = SQLAlchemy()


# Venue class model
class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }


# Event Registration Class Model
class EventRegistration(db.Model):
    __tablename__ = 'attendees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), unique=True, nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    company_size = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(250), nullable=False)
    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'job_title': self.job_title,
            'company_name': self.company_name,
            'company_size': self.company_size,
            'subject': self.subject,
        }


## Speaker Class
class Speaker(db.Model):
    __tablename__ = 'speakers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(100), nullable=False)
    speaker_avatar = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.astimezone)
    updated_at = db.Column(db.DateTime, default=datetime.astimezone, onupdate=datetime.astimezone)

    def __repr__(self):
        return f'<Speaker {self.name}>'
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'company': self.company,
            'position': self.position,
            'bio': self.bio,
            'speaker_avatar': self.speaker_avatar,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
    
  
