from django.db import models
from datetime import datetime

# Create your models here.

class ShowManager(models.Manager):
    def showValidator(self, postData):
        errors = {}
        newTitle = postData['title']
        shows = Show.objects.all()
        for show in shows.iterator():
            if newTitle == show.title:
                errors['title'] = "This title already exists"
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters long"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters long"
        if postData['releaseDate'] >= str(datetime.now()):
            errors['releaseDate'] = "Date must be set in the past"
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description must be at least 10 characters long"
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
