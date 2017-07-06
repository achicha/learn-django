from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'detail.html', {'album': album})
