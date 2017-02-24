from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user$', views.create),
    url(r'^return$', views.goback)
]
