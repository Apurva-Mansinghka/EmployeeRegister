from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

#view to show list of all details of all amployees
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employees/employee_list.html", context)


#view to add details of employee in database
def employee_form(request, id = 0 ):
    if request.method == "GET":
        if(id==0):
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form =  EmployeeForm(instance = employee)
        return render(request, "employees/employee_form.html", {'form': form})
    else:
        if(id == 0):
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,   instance = employee)

        if form.is_valid():
            form.save()
        return redirect('/employee/list')
        

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
