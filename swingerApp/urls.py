from django.conf.urls import url
from swingerApp import views
urlpatterns = [
	url(r'^$', views.swing),
]
