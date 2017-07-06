from django.conf.urls import url
from . import views                 # string view argument are deprecated

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),                          # /music/
    url(r'^(?P<album_id>\d+)/$', views.detail, name='detail'),      # /music/<album_id>/
]
