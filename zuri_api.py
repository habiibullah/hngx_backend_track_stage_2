#!/usr/bin/python3
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.url_map.strict_slashes = False

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off tracking modifications
db = SQLAlchemy(app)

# Define the SQLAlchemy model
class Person(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

# Helper function to validate input
def validate_input(data):
    return 'name' in data and isinstance(data['name'], str)

# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    name = data['name']
    if not validate_input(data):
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    try:
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return jsonify({'message': 'Person added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return make_response(jsonify({'error': 'User ID already exists'}), 400)

# READ: Fetching details of a person by name
@app.route('/api/<string:name>', methods=['GET'])
def read_person(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'name': person.name, 'user_id': person.user_id})

# UPDATE: Modify details of an existing person by name
@app.route('/api/<string:name>', methods=['PUT'])
def update_person(name):
    data = request.json
    if not validate_input(data):
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    try:
        person.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'})
    except IntegrityError:
        db.session.rollback()
        return make_response(jsonify({'error': 'User ID already exists'}), 400)

# DELETE: Remove a person by name
@app.route('/api/<string:name>', methods=['DELETE'])
def delete_person(name):
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

