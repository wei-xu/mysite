from django.db import models

# Create your models here.
# class Author(models.Model):
# 	"""docstring for Author"""
# 	name = models.CharField(max_length=40)
# 	def __str__(self):
# 		return self.name

class Blog(models.Model):
	"""docstring for Blog"""
	BELONGINGS = (
			('Pe','Personal'),
			('Pu','Public'),
		)
	title = models.CharField('title',max_length=60)
	author = models.CharField(max_length=40)
	belonging = models.CharField(max_length=20, choices=BELONGINGS, default=BELONGINGS[0][0])
	content = models.TextField()
	publish_time = models.DateTimeField('date published')
	def __str__(self):
		return self.title	
		