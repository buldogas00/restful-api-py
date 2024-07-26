
from flask import Flask, request, jsonify, abort  
from flask_sqlalchemy import SQLAlchemy  
from flask_httpauth import HTTPBasicAuth  
from config import Config  

app = Flask(__name__)  # 
app.config.from_object(Config)  # load config settings from config


db = SQLAlchemy(app)  


auth = HTTPBasicAuth() 

# create credentials for basic auth
@auth.verify_password
def verify_password(username, password):
    if username == app.config['AUTH_USERNAME'] and password == app.config['AUTH_PASSWORD']:
        return True  
    return False  

# create the employee model
class Employee(db.Model):
    __tablename__ = 'employees'  
    id = db.Column(db.Integer, primary_key=True)  # set the id column as an int and primary key (so no dupes, no nulls,etc.)
    name = db.Column(db.String(50), nullable=False)  # set the name, cannot be null
    department = db.Column(db.String(50), nullable=False)  
    workflow = db.Column(db.Float, nullable=True)  

# create the db and the table
with app.app_context():  # use flask app context
    db.create_all()  # create tables
    if not Employee.query.first():  # fetch first record to see if empty
        sample_employees = [
            Employee(name='Jonas Janauskas', department='CCB', workflow=11.0),
            Employee(name='Ruta Rutaute', department='CCB', workflow=22.3),
            Employee(name='Kastytis Kastauskas', department='CON', workflow=1.5),
            Employee(name='Juozas Juozutis', department='CON', workflow=1.8),
            Employee(name='Rokas Rokutis', department='CCB', workflow=2.5)
        ]
        db.session.bulk_save_objects(sample_employees)  # add sample employees to current db session
        db.session.commit()  # commit the current db session to save the changes to the db

# endpoint to retrieve all employees
@app.route('/employees', methods=['GET'])
@auth.login_required  # require authentication
def get_employees():
    employees = Employee.query.all()  # query all employees from the database
    return jsonify([e.as_dict() for e in employees])  # return the employees as a JSON response

# endpoint to retrieve an employee by id
@app.route('/employees/<int:id>', methods=['GET'])
@auth.login_required  
def get_employee(id):
    employee = Employee.query.get_or_404(id)  # query the employee by id, return 404 if not found
    return jsonify(employee.as_dict()) 

# endpoint to add a new employee
@app.route('/employees', methods=['POST'])
@auth.login_required 
def add_employee():
    data = request.get_json()  # get JSON data 
    if not data or 'name' not in data or 'department' not in data:  # validate the input data
        abort(400, description="Invalid input")
    new_employee = Employee(name=data['name'], department=data['department'], workflow=data.get('workflow'))  # create a new emp object (.get for wf, cuz might not be present when adding a new 1)
    db.session.add(new_employee)  
    db.session.commit()  # save
    return jsonify(new_employee.as_dict()), 201  # return as a JSON response with a 201

# endpoint to update an existing employee
@app.route('/employees/<int:id>', methods=['PUT'])
@auth.login_required 
def update_employee(id):
    employee = Employee.query.get_or_404(id)  
    data = request.get_json() 
    if not data: 
        abort(400, description="Invalid input")  
    employee.name = data.get('name', employee.name)  # update the name IF provided
    employee.department = data.get('department', employee.department)  
    employee.workflow = data.get('workflow', employee.workflow)  
    db.session.commit()  
    return jsonify(employee.as_dict())  

# endpoint to delete an employee
@app.route('/employees/<int:id>', methods=['DELETE'])
@auth.login_required 
def delete_employee(id):
    employee = Employee.query.get_or_404(id)  #
    db.session.delete(employee)  # delete the employee from the db session
    db.session.commit()  
    return jsonify({"message": "Employee deleted"})  # Return a JSON

# helper method to convert Employee objects to dictionaries
def as_dict(self):
    # create a dict with column names as keys and corresponding values from the Employee object
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# assign the helper to the Employee class
Employee.as_dict = as_dict

# run..
if __name__ == '__main__':
    app.run(port=app.config['PORT']) 
