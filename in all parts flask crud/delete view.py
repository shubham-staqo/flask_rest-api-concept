from django.shortcuts import redirect


@app.route('/data/<init:id>delete' methods=['GET','POST'])
def delete():
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == "POST":
        if employee:
             db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        abort(404)
        return render_template('delete.html')