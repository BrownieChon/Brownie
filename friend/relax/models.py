from django.db import models

# Create your models here.
class relax(models.Model):
  name = models.CharField(max_length=255)
  message = models.CharField(max_length=1000)