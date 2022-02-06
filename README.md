# EmployeeRegister

A web app to add/view/delete/update employees in employee table suing django-python framework.
Database used is PostgreSQL with details as : 

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'akratech_employees',
        'USER' : 'postgres',
        'PASSWORD': 'admin',
        'HOST' : 'localhost'
        
At command prompt go the root folder and execute commands as :
>>python manage.py runserver

After the server is up
on browser open- 
http://localhost:8000/employee/

This will open frm to add new employee details
To check all employees use URL - 
http://localhost:8000/employee/list/

It has edit and delete buttons at end of each employee that performs respective operations.
Add new button also on top right to add new record of employee
Drop down used to add blood group which is foreign ket from another table.
