import os
from flask import Flask
from flask_migrate import Migrate, upgrade
from models import db, Venue, EventRegistration, Speaker  # adjust as needed

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bizza.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

def run_migration():
    with app.app_context():
        if os.path.exists("migrations"):
            print("🔄 Migrations folder found. Applying latest migration...")
            upgrade()
            print("✅ Database upgraded.")
        else:
            print("⚠️ No migration folder found. Creating all tables directly...")
            db.create_all()
            print("✅ Tables created using create_all().")

if __name__ == "__main__":
    run_migration()