from turtle import position
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from django.shortcuts import redirect


@app.route('/data/create/', methods = ['GET', 'POST'])

def create():
    if request == 'GET':
        return render_temeplate('create.html')

    if request == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id = employee_id, name = name, age = age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')