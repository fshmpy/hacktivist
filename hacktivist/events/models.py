from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=256)
    date_time = models.DateTimeField()
    description = models.TextField()
