from django.urls import include
from django.conf.urls import url

from .views import postListView,postDetailView


app_name = "post"
urlpatterns = [
    url(r'^$', postListView.as_view(), name = 'post_list'),
    url(r'^(?P<slug>[\w-]+)/$', postDetailView.as_view(), name = 'post_detail'),
]
