from django.conf.urls import url
from swingerApp import views
urlpatterns = [
	url(r'^swing$', views.swing),
	url(r'^bulkswing$', views.bulk_swing),
]
