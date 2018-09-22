from django.urls import include
from django.conf.urls import url

from .views import postListView,postDetailView,PostCreateView,AuthorPostView


app_name = "post"
urlpatterns = [
    url(r'^$', postListView.as_view(), name = 'post_list'),
    url(r'^create/$', PostCreateView.as_view(), name = 'post_create'),
    url(r'^mypost/$', AuthorPostView.as_view(), name = 'my_post'),
    url(r'^(?P<slug>[\w-]+)/$', postDetailView.as_view(), name = 'post_detail'),
]
