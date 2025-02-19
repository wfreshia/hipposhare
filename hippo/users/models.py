from django.db import models
from django.contrib.auth.models import AbstractUser
from health_info_exchange.models import Hospital
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin','Admin'),
        ('patient', 'Patient')
    ]
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    roles = models.CharField(choices=ROLE_CHOICES,max_length=20,default='patient')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return f"{self.email} - {self.role}"

