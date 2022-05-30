from flask import render_template


@app.route('/data')
def RetrieveDataList():
    emoloyees = EmployeeModel.query.all()
    return render_template('datalist.html', employees = employees)