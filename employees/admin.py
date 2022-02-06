from django.contrib import admin

# Register your models here.
from .models import BloodGroup, Employee
admin.site.register(Employee)
admin.site.register(BloodGroup)