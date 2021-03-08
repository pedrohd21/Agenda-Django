from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.CharField(max_length=70, blank=True)
    creation_data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.contact_name
    
