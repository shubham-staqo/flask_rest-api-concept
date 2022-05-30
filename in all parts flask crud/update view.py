@app.route('/data/<init:id>/update' , methods = ['GET', 'POST'])


def update(id):
       employee = EmployeeModel.query.filter_by(employee_id = id).first()
       if request.method == "POST"
          if employee:
             db.session.delete(employee)
             db.session.commit()

            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(name = name, age = age, position = position)
             db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('update.html', employee = employee)

             

