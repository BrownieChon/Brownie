from django.db import models

# Create your models here.
class relax(models.Model):
  user = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  repassword = models.CharField(max_length=255)
      
class talk(models.Model):
  user = models.CharField(max_length=255)
  message = models.CharField(max_length=1000)

