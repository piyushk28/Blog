from django.urls import path,include

from .views import author_edit_view


app_name = "authorprofile"
urlpatterns = [
    path('edit/', author_edit_view, name = 'edit_author'),
]	
