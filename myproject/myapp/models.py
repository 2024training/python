from django.db import models
from django.utils import timezone

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="監督")
    def _str_(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    watch_data = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="監督", related_name='movie')
    def _str_(self):
        return self.name

class Log(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="タイトル", related_name='log')

    def _str_(self):
        return self.name

# Create your models here.
