from django.db import models
from django.utils import timezone


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    email = models.CharField(max_length=70, blank=True)
    creation_data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.contact_name
    
