from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Info(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Contact_Number = models.CharField(max_length=50)
    Whatsapp_Number = models.CharField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Company_Registration_Number = models.CharField(max_length=50)
    Company_VAT_Number = models.CharField(max_length=50)
    Company_Address = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)

    def __str__(self):
        return self.username.first_name + self.username.last_name
    