# news/models.py

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.title
