# restful-api-py
A simple RESTful API made with Flask that can be containerized with basic authentication.

## Project Structure
```sh
project-directory/
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
```

## Setup Instructions
Ensure you have the following installed on your machine:

Python 3.9 or higher

Docker (if you choose to run the application in a Docker container)

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/tices/restful-api-py.git

## Running the application without Docker

**Install dependencies**:
```sh
pip install -r requirements.txt
```

 **Navigate to the directory of the API, and run it**:
```sh
cd <path_to_API>
python app.py
```

## Running the Application with Docker

**Build the Docker Image**:

```sh
docker build -t flask-api .
```

**Run the Docker Container editing the port as needed**:

```sh
docker run -p [PORT]:[PORT] flask-api
```

## CRUD operations

You can perform CRUD operations using Postman, or any other REST client.

if using cURL, when performing POST or PUT operations, don't forget that you must pass a "Content-Type: application/json" header along with the request.

## Using Postman

**Get All Employees**:
```sh
URL: http://127.0.0.1:1111/employees
Authorization: Basic Auth (username:password)
```

**Get Employee by ID**:
```sh
URL: http://127.0.0.1:1111/employees/{id}
Authorization: Basic Auth (username:password)
```

**Add New Employee**:
```sh
URL: http://127.0.0.1:1111/employees
Authorization: Basic Auth (username:password)
Body: JSON
{
  "name": "---",
  "department": "---",
  "workflow": -
}
```
**Update Employee**:
```sh
URL: http://127.0.0.1:1111/employees/{id}
Authorization: Basic Auth (username:password)
Body: JSON
{
  "name": "---",
  "department": "---",
  "workflow": -
}
```

**Delete Employee**:

```sh
URL: http://127.0.0.1:1111/employees/{id}
Authorization: Basic Auth (username:password)
```
