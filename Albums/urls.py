from django.urls import path

from . import views
urlpatterns = [
    
    path('add/', views.add_album,name = 'album'),
    path('edit/<int:id>', views.edit_album,name = 'edit'),
    path('delete/<int:id>', views.delete_album,name = 'delete'),
]
