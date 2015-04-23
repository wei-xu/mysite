from django.db import models
from datetime import datetime
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
	publish_time = models.DateTimeField('date published', default=datetime.now)
	def __unicode__(self):
		return self.title	


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m')
    upload_time = models.DateTimeField('date uploaded', default=datetime.now)
    uploader = models.CharField('uploader', max_length=40, default='undefined')
    def __unicode__(self):
    	return self.docfile.name.split('/')[-1]
