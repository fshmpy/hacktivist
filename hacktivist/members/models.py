from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    org = models.ForeignKey('organizations.Community', on_delete=models.SET_NULL, null=True)
    occupation = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    dob = models.DateField()
    int_domain = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    gitlab = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    osm_id = models.CharField(max_length=255)
    os = models.CharField(max_length=255)

    def __str__(self):
        return str(user.first_name + user.last_name)
