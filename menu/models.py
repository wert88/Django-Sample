from django.db import models
from django.utils import timezone
from django.urls import reverse

class Album(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	year = models.CharField(max_length=200)
	time = models.DateTimeField(default=timezone.now)
	pic = models.FileField()
	
	def get_absolute_url(self):
		return reverse('index')

	def __str__(self):
		return self.title

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	name = models.CharField(max_length=200)
	audio = models.FileField()
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name