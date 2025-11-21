#test_empdetails.py
import pytest
from empdetails import get_employee_info
def test_get_employee_info():
    #sample data
    name = "Harshita"
    emp_id = "E101"
    department = "IT"
    salary = 55000
    #expected output
    expected_output = (
        "Employee Name: Harshita\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    #assertion
    assert get_employee_info(name, emp_id, department, salary) == expected_output
    