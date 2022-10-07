from datetime import datetime
from django.db import models

# Create your models here.
class LanguagesModel(models.Model):
    name = models.TextField(max_length = 200)
    iso_code = models.TextField()
 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name

class VotesModel(models.Model):
    rating = models.SmallIntegerField( default=1, blank=True)
    ip = models.TextField(blank=True)
    date_time = models.DateTimeField(auto_now_add = True)

 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.type