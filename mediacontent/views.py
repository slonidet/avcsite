from django.shortcuts import render
from .models import Album, Video, AlbumPhoto
# Create your views here.
def media(request):
    album = Album.objects.all().order_by('-date_album')
    video = Video.objects.all().order_by('-date')
    return render(request,"media.html",{"album": album, "video": video})

def photo_view(request, album_pk=1):
    album = Album.objects.get(id=album_pk)
    other = Album.objects.exclude(id=album_pk)[:5]
    photos = AlbumPhoto.objects.filter(album_id=album_pk).order_by('title')

    return render(request, "photo.html", {"photos":photos, "album":album, "other":other})

def video_view(request, video_pk=1):
    video = Video.objects.get(id=video_pk)
    other = Video.objects.exclude(id=video_pk)[:5]
    return render(request, "video.html", {"video": video, "other":other})