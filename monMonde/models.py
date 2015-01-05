from django.db import models
import datetime
from django.utils import timezone
# Create your views here.
class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('monMonde.Category')
	def __unicode__(self):
		return '%s' % self.title

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	def __unicode__(self):
		return '%s' % self.title

class Nom(models.Model):
	nom=models.CharField(max_length=30)
	def __unicode__(self):
		return '%s' % self.nom
