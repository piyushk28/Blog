from django.urls import path,include

from .views import AuthorEditView


app_name = "authorprofile"
urlpatterns = [
    path('edit/', AuthorEditView.as_view(), name = 'edit_author'),
]	
