from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length = 200)	
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now()  - datetime.timedelta(days = 1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text

class Person(models.Model):
	"""docstring for Person"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(Person, through='Membership')	
	def __str__(self):
		return self.name

class Membership(models.Model):
	person = models.ForeignKey(Person)
	group = models.ForeignKey(Group)
	date_joined = models.DateField()
	invite_reason = models.CharField(max_length=64)