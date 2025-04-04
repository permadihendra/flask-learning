from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Connection using SQLAlchemy flask_sqlalchemy
# database : sqllite

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bizza.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create Venue class model
class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }


# Applications API Routing
# ------------------------
@app.route('/')
def index():
    return 'Welcome to Bizza REST API Server'

## venues API Endpoint
# @app.route('/api/v1/venues')
# def venues():
#     return jsonify({
#         "id": 1,
#         "name": "Auditorium A"
#     }), 200

## Venues API Endpont -> add new venue
@app.route('/api/v1/venues', methods=['POST'])
def add_venues():
    if request.method == 'POST':
        name = request.get_json().get('name')
        all_venues = Venue.query.filter_by(name=name).first()
        if all_venues:
            return jsonify(message="Venue name already exist!"), 409
        else:
            new_venue =  Venue(name=name)
            db.session.add(new_venue)
            db.session.commit()
            return jsonify({
                'success' : True,
                'venues': new_venue.format()
            }), 201
        
## Venues API endpoint -> retrieve all the venues in database
@app.route('/api/v1/venues', methods=['GET'])   
def retrieve_venues():
    if request.method == 'GET':
        all_venues = Venue.query.all()
        if all_venues:
            return jsonify({
                'success': True,
                'venues': [venue.format() for venue in all_venues]
            }), 200
        else:
            return jsonify(message="No venue record found!"), 404
        
## Venues API Endpoint --> return single venue
@app.route('/api/v1/venues/<int:id>', methods=['GET'])
def retrieve_venue(id):
    if request.method == 'GET':
        venue = Venue.query.filter(Venue.id == id).first()
        if venue:
            return jsonify({
                'success': True,
                'venue': venue.format()
            }), 200
        else:
            return jsonify(message="Record id not found"), 404

## Venues API Endpoint --> update single venue record
@app.route('/api/v1/venues/<int:id>', methods=['PUT'])
def update_venue(id):
    if request.method == 'PUT':
        name = request.get_json().get('name')
        venue = Venue.query.get(id)
        if not venue:
            return jsonify(message="Venue record not found"), 404
        else:
            venue.name = name
            db.session.commit()
            return jsonify({
                'success': True,
                'updated venue': venue.format()
            }), 200
        
## Venues API Endpoint --> delete single venue record
@app.route('/api/v1/venues/<int:id>', methods=['DELETE'])
def remove_venue(id):
    if request.method == 'DELETE':
        venue = Venue.query.filter(Venue.id==id).first()
        if venue:
            db.session.delete(venue)
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'You deleted a venue',
                'deleted': venue.format()
            }), 202
        else:
            return jsonify(message="That venue does not exist"), 404

# @app.route('/api/v1/speakers/')
# def speakers():
#     firstname = request.args.get("firstname")
#     lastname = request.args.get("lastname")
#     if firstname is not None and lastname is not None:
#         return jsonify(message="The speaker's fullname : "+firstname+" "+lastname)
#     else:
#         return jsonify(message="No query parameters in the url")

@app.route('/api/v1/speakers/<int:speakerId>')
def getSpeaker(speakerId):
     # Simulated data lookup
    speakers = {
        1: {"id": 1, "name": "John Doe", "topic": "AI"},
        2: {"id": 2, "name": "Jane Smith", "topic": "Cybersecurity"}
    }

    speakerData = speakers.get(speakerId)

    if speakerData:
        return jsonify(speakerData)
    else:
        return jsonify({"error": "Speaker not found"}), 404

if __name__ == '__main__':
    app.run()