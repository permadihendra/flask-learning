# Import the shared db instance
from app.models import db


class EventRegistration(db.Model):
    __tablename__ = "attendees"
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
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "job_title": self.job_title,
            "company_name": self.company_name,
            "company_size": self.company_size,
            "subject": self.subject,
        }
