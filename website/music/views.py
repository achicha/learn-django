from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    error_message = ''
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        error_message = "you did not select a valid song"
        return render(request, 'detail.html', {'album': album,
                                               'error_message': error_message},)
    else:
        if not selected_song:
            selected_song.is_favorite = True
            selected_song.save()
        else:
            error_message = 'this song is already in your Favorites'
        return render(request, 'detail.html', {'album': album, 'error_message': error_message})
