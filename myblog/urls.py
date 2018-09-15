"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from .views import about_page,home_page
from post.views import postListView,postDetailView
from categories.views import categoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_page, name = 'about'),
    path('', home_page, name='home'),
    path('category/<slug>/', categoryView.as_view(), name='category'),
    # path('category/', categoryListView.as_view(), name='category2'),
    path('', include('post.urls',namespace ='post')),
]
