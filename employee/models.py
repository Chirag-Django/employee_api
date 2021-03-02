from django.db import models

POSITION_CHOICES = (
    ('team_lead','Team Lead'),
    ('project_manager', 'Project Manager'),
    ('software_engineer','Software Engineer'),
    ('tester','Tester')
)

# Create your models here.
class Employee(models.Model):
    '''Model Definition for Employee'''
    emp_no = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=500)
    emp_salary = models.IntegerField()
    emp_position = models.CharField(max_length=30, choices=POSITION_CHOICES,default='software_engineer')
    emp_present = models.BooleanField(default=True,null=True)

    def __str__(self):
        return str(self.emp_no)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    # Instance Method to get current status of employee
    def get_status(self):
        if self.emp_present:
            return "Present"
        return "Absent"