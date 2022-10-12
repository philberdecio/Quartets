from django.db import models
import time

# Create your models here.

class Folio(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Quartet(models.Model):
    name = models.CharField(max_length=250)
    folio = models.ForeignKey(Folio, on_delete=models.CASCADE, related_name="quartets")

    def __str__(self):
        return self.name

class Entry (models.Model):
    type = models.CharField(max_length=100)
    url = models.TextField(max_length=None, blank=True)
    text = models.TextField(max_length=None, blank=True)
    annote = models.TextField(max_length=150, blank=True)
    quartet = models.ForeignKey(Quartet, on_delete=models.CASCADE, related_name="entries")

    def __str__(self):
        return self.name
