from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     url(r'^HOME', views.index, name='index'),
    url(r'^add_info$', views.add_info, name='add_info'),
    url(r'^delete_info$', views.delete_info, name='delete_info'),
    url(r'^score_detail', views.score_detail, name='score_detail'),
    url(r'^update_score', views.update_score, name='update_score'),
    url(r'^update_all', views.update_all, name='update_all'),
]