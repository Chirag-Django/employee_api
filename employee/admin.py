from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_no','emp_name','emp_position','emp_salary','emp_address','emp_present']

admin.site.register(Employee,EmployeeAdmin)

