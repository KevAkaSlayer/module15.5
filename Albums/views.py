from django.shortcuts import render,redirect
from . forms import AlbumForm
from . models import album_model 
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()

    return render (request,'album.html',{'form':form})

def edit_album(request,id):
    album = album_model.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance = album)
        if form.is_valid() :
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()

    return render (request,'album.html',{'form':form})

def delete_album(request,id):
    album = album_model.objects.get(pk=id)
    album.delete()

    return redirect('home')