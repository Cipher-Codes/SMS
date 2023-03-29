from django.db import models

# Create your models here.
class AdminLoginDetails(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.username
    
class StaffDetails(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    monday = models.IntegerField(default=0)
    tuesday = models.IntegerField(default=0)
    wednesday = models.IntegerField(default=0)
    thursday = models.IntegerField(default=0)
    friday = models.IntegerField(default=0)
    saturday = models.IntegerField(default=0)

    def __str__(self):
        return self.fullname


