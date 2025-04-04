from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Bizza REST API Server'

@app.route('/api/v1/venues')
def venues():
    return jsonify({
        "id": 1,
        "name": "Auditorium A"
    }), 200

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