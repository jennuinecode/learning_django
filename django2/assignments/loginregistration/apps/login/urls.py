from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^login/(?P<commonroom>[a-zA-Z]+)$', views.login),
    url(r'^register$', views.register),
    url(r'^add$', views.add),

]
