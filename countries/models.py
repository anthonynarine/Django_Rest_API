from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=50, blank=False, default="")
    capital = models.CharField(max_length=50, blank=False, default="")
      
    #django will automatically add an auto-increment integer pk column named id
    #the subclass below will sort our db records in acending order whe a query is made
    
    class Meta:
        ordering = ("id", )