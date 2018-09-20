from django.urls import include
from django.conf.urls import url


from .views import author_edit_view,AuthorDetailView


app_name = "authorprofile"
urlpatterns = [
    url(r'^edit/$', author_edit_view, name = 'edit_author'),
    url(r'^profile/$', AuthorDetailView.as_view(), name = 'profile'),
]	
