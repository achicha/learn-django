from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'music.views.index', name='index'),
]
