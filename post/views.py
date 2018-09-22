from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.http import Http404
from django.views.generic import ListView, DetailView,CreateView
from django.urls import reverse_lazy

from .forms import PostCreateForm
from .models import Post


class postListView(ListView):
	template_name = "post/post_list.html"

	def get_queryset(self, *args, **kwargs):
		request=self.request
		qs=Post.objects.filter(active=True)
		if qs.exists():
			print('exist')
			return qs
		else:
			print("don't exist")
			return None


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


class PostCreateView(LoginRequiredMixin,CreateView):
	form_class = PostCreateForm
	template_name = 'post/create.html'
	def form_valid(self,form):
		request=self.request
		form.save(request=request)
		return redirect('post:post_list')

class AuthorPostView(ListView):
	template_name = "post/post_list.html"

	def get_queryset(self, *args, **kwargs):
		request=self.request
		user= request.user
		qs=Post.objects.filter(author=user)
		if qs.exists():
			return qs
		else:
			return None