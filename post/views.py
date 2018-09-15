from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Post


class postListView(ListView):
	template_name = "post/post_list.html"

	def get_queryset(self, *args, **kwargs):
		request=self.request
		return Post.objects.all()


class postDetailView(DetailView):
	queryset = Post.objects.all()
	template_name = "post/post_detail.html"

	def get_object(self, *args, **kwargs):
		request=self.request
		slug = self.kwargs.get('slug')

		try:
			instance = Post.objects.get(slug__exact =slug,active=True)

		except Post.DoesNotExist:
			return Http404("Post Does Not Exist")

		except Post.MultipleObjectsReturned:
			qs =Post.objects.filter(slug__exact=slug,active=True)
			instance= qs.first()

		except:
			raise  Http404("Bad Request")

		return instance