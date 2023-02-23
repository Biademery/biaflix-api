from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=300)
    movieURL = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.name 