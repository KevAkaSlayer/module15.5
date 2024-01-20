from django.shortcuts import render,redirect
from . models import musician_model
from . forms import MusicianForm
# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = MusicianForm()
    return render(request,'musician.html',{'form':form})


def edit_musician(request,id):
    musician = musician_model.objects.get(pk = id)
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST,instance = musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = MusicianForm()
    return render(request,'musician.html',{'form':form})

def delete_musician(request,id):
    musician = musician_model.objects.get(pk = id)
    musician.delete()

    return redirect('home')