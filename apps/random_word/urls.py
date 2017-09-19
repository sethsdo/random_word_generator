from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^random/$', views.index),     # This line has changed!
    url(r'^generate/$', views.generate),
    url(r'^random/reset/$', views.resetWord),
]
