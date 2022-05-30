from flask import render_template


@app.route('/data/<init:id>')
def RetrieveSingleEmployee():
    employee = EmployeeModel.query.filter_)by(employee_id = id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id = {id} doesn't Exits."