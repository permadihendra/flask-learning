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

@app.route('/api/v1/speakers/')
def speakers():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    if firstname is not None and lastname is not None:
        return jsonify(message="The speaker's fullname : "+firstname+" "+lastname)
    else:
        return jsonify(message="No query parameters in the url")

if __name__ == '__main__':
    app.run()