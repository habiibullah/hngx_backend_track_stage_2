# Person API Documentation

This document provides detailed information about the Person API, including standard request and response formats, sample usage, known limitations, and setup instructions.

## Standard Request and Response Formats

### Create a New Person

- **Endpoint**: `/api`
- **HTTP Method**: POST
- **Request Format**:
  - Content-Type: application/json
  - Request Body:
    ```json
    {
      "name": "string"
    }
    ```
- **Response Format**:
  - HTTP Status: 201 Created
  - Response Body:
    ```json
    {
      "message": "Person added successfully"
    }
    ```

### Fetch Details of a Person

- **Endpoint**: `/api/<name>`
- **HTTP Method**: GET
- **Response Format**:
  - HTTP Status: 200 OK
  - Response Body:
    ```json
    {
    "name": "John Doe",
    "user_id": 1
}

    ```

### Modify Details of an Existing Person

- **Endpoint**: `/api/<name>`
- **HTTP Method**: PUT
- **Request Format**:
  - Content-Type: application/json
  - Request Body:
    ```json
    {
      "name": "string"
    }
    ```
- **Response Format**:
  - HTTP Status: 200 OK
  - Response Body:
    ```json
    {
      "message": "Person updated successfully"
    }
    ```

### Remove a Person

- **Endpoint**: `/api/<name>`
- **HTTP Method**: DELETE
- **Response Format**:
  - HTTP Status: 200 OK
  - Response Body:
    ```json
    {
      "message": "Person deleted successfully"
    }
    ```

## Sample Usage

Here are some sample usage scenarios for the API:

### Create a New Person

**Request:**

```bash

curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe"}' http://localhost:5000/api

### Fetch Person Details by Name

**Request:**

curl http://localhost:5000/api/John%20Doe

### Modify Person Details by Name

**Request**

curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:5000/api/John%20Doe

### Remove a Person by Name

**Request**

curl -X DELETE http://localhost:5000/api/Updated%20Name

