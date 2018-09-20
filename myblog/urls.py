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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.conf.urls import url

from django.contrib.auth.views import LogoutView,LoginView
from .views import about_page,home_page
from post.views import postListView,postDetailView
from categories.views import categoryView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', about_page, name = 'about'),
    url(r'^$', home_page, name='home'),
    url(r'^category/(?P<slug>[\w-]+)/$', categoryView.as_view(), name='category'),
    url(r'^login/$',LoginView.as_view(
                                    redirect_authenticated_user=True,
                                    template_name='accounts/login.html',
                                    ),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^posts/', include('post.urls',namespace ='post')),
    url(r'^author/', include('authorprofile.urls',namespace ='authorProfile')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
