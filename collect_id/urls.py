from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_info$', views.add_info, name='add_info'),
    url(r'^delete_info$', views.delete_info, name='delete_info'),
]