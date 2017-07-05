from django.conf.urls import url
from . import views                 # string view argument are deprecated


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
