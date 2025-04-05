from datetime import datetime

## Speaker Class
class Speaker(db.Model):
    __tablename__ = 'speakers'
    id = db.Column(db.Integer, primary_ke=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(100), nullable=False)
    speaker_avatar = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)
    updated_at = db.Column(db.DateTime, default=datetime.timezone.utc, onupdate=datetime.timezone.utc)

    def __repr__(self):
        return f'<Speaker> {self.name}'
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
    
  
