from django.db import models
from datetime import datetime

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    dni = models.CharField(max_length=10, unique=True)
    date_joined = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveBigIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    status = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta():
        db_table = 'employees'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

