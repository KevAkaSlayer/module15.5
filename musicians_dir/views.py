from django.shortcuts import render
from Albums.models import album_model

def home(request):
    data = album_model.objects.all()
    return render(request,'home.html',{'data':data})