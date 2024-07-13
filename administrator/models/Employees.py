from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    image = models.ImageField(upload_to='employees/', null=True, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name