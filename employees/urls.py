from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.employee_form,name = 'employee_insert'), #for inserting new employee record
    path('delete/<int:id>/' , views.employee_delete ,name = 'employee_delete'), #for deleting an employee record
    path('<int:id>/', views.employee_form,name = 'employee_update'), #for updating employee
    path('list/', views.employee_list,name = 'employee_list') #to retrieve and display employee records
    
]
