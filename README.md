Person API

The Person API is a simple Flask-based API that allows you to perform CRUD (Create, Read, Update, Delete) operations on a person resource. This README will guide you through setting up, running, and using the API.

Table of Contents

Prerequisites
Setup
Running the API
API Endpoints
Create a New Person
Fetch Details of a Person
Modify Details of an Existing Person
Remove a Person
Automated Testing
Contributing
License

Prerequisites

Before you can set up and run the API, make sure you have the following prerequisites installed on your system:

Python 3.x
Flask
SQLite

You can install Flask using pip:

pip install flask

sudo apt install sqlite3

Setup

1. Clone this repository to your local machine:

https://github.com/habiibullah/hngx_zuri_stage_2.git

2. Navigate to the project directory:

cd hngx_zuri_stage_2

3. Install the required Python packages:

pip install -r requirements.txt

Running the API

Make sure you are in the project directory with your virtual environment activated.

Run the API using the following command:

python zuri_api.py

API Endpoints

The API provides the following endpoints for CRUD operations on the person resource:

Create a New Person
Endpoint: /api

HTTP Method: POST

Request Body: JSON object with a "user_id" field.

Example Request:

curl -X POST -H "Content-Type: application/json" -d '{"user_id":"John Doe"}' http://localhost:5000/api

Example Response

{"message": "Person added successfully"}

Fetch Details of a Person

Endpoint: /api/<name>

HTTP Method: GET

Example Request:

curl http://localhost:5000/api/John%20Doe

Example Response

{"user_id": "John Doe"}

Modify Details of an Existing Person

Endpoint: /api/<name>

HTTP Method: PUT

Request Body: JSON object with a "user_id" field containing the updated user_id.

Example Request:

curl -X PUT -H "Content-Type: application/json" -d '{"user_id":"Jane Smith"}' http://localhost:5000/api/John%20Doe

Example Response

{"message": "Person updated successfully"}

Remove a Person

Endpoint: /api/<name>

HTTP Method: DELETE

Example Request:

curl -X DELETE http://localhost:5000/api/Jane%20Smith

Example Response

{"message": "Person deleted successfully"}

Automated Testing

To automate testing of the API, you can use the provided Python script (test_api.py) in the project directory. This script covers each CRUD operation.

Run the script as follows:

python test_api.py

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

