# Import Django Settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Company.settings')
import django
django.setup()

# Import Faker Module
from faker import Faker
from employee.models import Employee
from random import *

#Create Faker Object
fake = Faker()


# Create Random 3 digits String to represent employee number
def random_emp_no_generator():
    num = str()
    for i in range(3):
        num += str(randint(0,9))
    return num

# Create Random 5 digits String to represent employee Salary
def random_emp_salary_generator():
    num = str()
    for i in range(5):
        num += str(randint(1,9))
    return num

# Create Fake Presentee -- True or False
def random_emp_status_generator():
    present = fake.random_int(0,1)
    if present:
        return True
    return False

# Function to Create Fake Employee data-->  input 'n' represents no of employee to be created
def populate(n:int):
    for i in range(n):
        emp_no = int(random_emp_no_generator())
        emp_name = fake.name()
        emp_salary = int(random_emp_salary_generator())
        emp_address = fake.address()
        emp_position = fake.random_element(elements=('team_lead',
                                                     'project_manager',
                                                     'software_engineer',
                                                     'tester'))
        emp_present = random_emp_status_generator()
        employee_record = Employee.objects.get_or_create(emp_no=emp_no,
                                                         emp_name=emp_name,
                                                         emp_address=emp_address,
                                                         emp_salary=emp_salary,
                                                         emp_position=emp_position,
                                                         emp_present=emp_present)

populate(15)
