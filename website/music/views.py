from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }

    return render(request, 'index.html', context)


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: {} </h2>".format(str(album_id)))
