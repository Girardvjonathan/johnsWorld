from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from monMonde import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='Index'),
	url(r'^media$', views.MediaView.as_view(), name='Media'),
	url(r'^programming$', views.ProgrammingView.as_view(), name='Programming'),
	url(r'^server$', views.ServerView.as_view(), name='Serveur'),
	url(r'^book$', views.BookView.as_view(), name='Book'),
)