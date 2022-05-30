from enum import unique
from turtle import position
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "table"

id = db.column(db.integer, primary_key = True)
employee_id = db.column(db.interger(), unique = True)
name = db.column(db.string())
age = db.column(db.interger())
position = db.column(db.interger())

def __init__(self, employee_id, name, age, position):
    self.employee_id = employee_id
    self.name = name
    self.age = age 
    self.postion = position

def __repr__(self):
    return f"{self.name}:{self.employee_id}"
