from django.utils import timezone

from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255, default='')
    photo = models.ImageField(upload_to='actors/', null=True)
    date_of_birth = models.DateField(default=timezone.now)
    place_of_birth = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True, blank=True, related_name='actors')
    bio = models.TextField(default='')

    # filmography

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.FloatField()

    def __str__(self):
        return f' {self.name} ({self.pk})'


class Title(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    storyline = models.TextField(default='')
    stars = models.ManyToManyField(Actor, related_name='filmography')
    genres = models.ManyToManyField('Genre', related_name='titles')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)
    # tags

    def __str__(self):
        return self.name
