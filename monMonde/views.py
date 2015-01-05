from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from monMonde.models import Blog, Nom

class IndexView(generic.ListView):
    template_name = 'johnsprojects/index.html'
    context_object_name = 'nom'
    def get_queryset(self):
        return Nom.objects.all()
class MediaView(generic.ListView):
	context_object_name = 'nom'
	template_name = 'johnsprojects/media.html'
	def get_queryset(self):
		return Nom.objects.all()
class ProgrammingView(generic.ListView):
	context_object_name = 'nom'
	template_name = 'johnsprojects/programming.html'
	def get_queryset(self):
		return Nom.objects.all()
class ServerView(generic.ListView):
	context_object_name = 'nom'
	template_name = 'johnsprojects/server.html'
	def get_queryset(self):
		return Nom.objects.all()
class BookView(generic.ListView):
	context_object_name = 'blog'
	template_name = 'johnsprojects/book.html'
	def get_queryset(self):
		return Blog.objects.all()