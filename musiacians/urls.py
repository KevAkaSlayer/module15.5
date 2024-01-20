from django.urls import path

from . import views
urlpatterns = [
    path('addm/', views.add_musician,name = 'addm'),
    path('editm/<int:id>', views.edit_musician,name = 'editm'),
    path('delm/<int:id>', views.delete_musician,name = 'delm'),
]
