from django.conf.urls import url
from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name="confirm"),

]
