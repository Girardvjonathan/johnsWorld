from django.contrib import admin
from monMonde.models import Blog, Category
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.



admin.site.register(Blog)
admin.site.register(Category)