from django.db import models
from django.utils import timezone

class Ticket(models.Model):
    title = models.CharField(max_length=30, blank=False)
    summary = models.CharField(max_length=100, blank=False)
    detail = models.TextField()
    image = models.ImageField(upload_to='media/img')
    date = models.DateField()
    
    def __str__(self):
        return self.name
 