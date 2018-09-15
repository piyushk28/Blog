from django.urls import path,include

from .views import postListView,postDetailView


app_name = "post"
urlpatterns = [
    path('posts/', postListView.as_view(), name = 'post_list'),
    path('<slug>/', postDetailView.as_view(), name = 'post_detail'),
]
