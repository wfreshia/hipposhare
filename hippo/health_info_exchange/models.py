from django.db import models

# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    hospital_location = models.TextField()
    contact_email = models.EmailField(unique=True)
    hospital_contact = models.CharField(max_length=20)
    hospital_code =  models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.hospital_name
    
    