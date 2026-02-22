from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # This ensures Django doesn't create a 'Person' table

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hired_on = models.DateField()
    is_active = models.BooleanField(default=True)
    
    # NEW: The employee's salary
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Client(Person):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    lead_source = models.CharField(max_length=100, blank=True, null=True)
    
    # Status helps track the sales funnel
    STATUS_CHOICES = [
        ('LEAD', 'Lead'),
        ('ACTIVE', 'Active'),
        ('PAST', 'Past'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='LEAD')
    
    # NEW: How much the company gets from the client
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)