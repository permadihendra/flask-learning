# Import the shared db instance
from app.models import db


class Venue(db.Model):
    __tablename__ = "venues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def format(self):
        return {"id": self.id, "name": self.name}
