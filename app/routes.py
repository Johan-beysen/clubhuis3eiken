from flask import Blueprint, render_template, flash, redirect, url_for
from app.models import Employee
from app.forms import EmployeeForm
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(name=form.name.data, email=form.email.data)
        db.session.add(employee)
        db.session.commit()
        flash('Employee added successfully!')
        return redirect(url_for('main.add_employee'))
    return render_template('add_employee.html', form=form)

@bp.route('/employees')
def employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)