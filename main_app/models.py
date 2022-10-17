from django.db import models
import time
from django.contrib.auth.models import User

# Create your models here.

class Folio(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

class Quartet(models.Model):
    name = models.CharField(max_length=250)
    folio = models.ForeignKey(Folio, on_delete=models.CASCADE, related_name="quartets")

    def __str__(self):
        return self.name

class Entry (models.Model):
    embed = models.TextField(max_length=None, blank=True)
    image = models.TextField(max_length=None, blank=True)
    text = models.TextField(max_length=None, blank=True)
    annotate = models.TextField(max_length=150, blank=True)
    quartet = models.ForeignKey(Quartet, on_delete=models.CASCADE, related_name="entries")
