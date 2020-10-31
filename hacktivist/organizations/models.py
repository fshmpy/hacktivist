from django.db import models

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True, max_length=30)
    acronym = models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return str(self.name + " (" + self.acronym +")")
