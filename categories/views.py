from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from post.models import Post
from .forms import CategoryForm
from .models import Category

# Create your views here.
class categoryView(ListView):
	template_name = "post/post_list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(categoryView,self).get_context_data(*args, **kwargs)
		request =self.request
		category_slug  = self.kwargs.get("slug")
		try:
			instance = Category.objects.get(slug__exact = category_slug)
		except Category.DoesNotExist:
			raise Http404(" Category Not found")

		except Category.MultipleObjectReturned:
			qs = Category.objects.filter(slug__exact = category_slug)
			instance = qs.first()

		except:
			raise Http404("Bad request")

		context['category_name'] = instance.title

		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		category_slug  = self.kwargs.get("slug")
		post_qs = Post.objects.filter(category__slug__exact = category_slug)
		return post_qs

def add_category_view(request):
	form = CategoryForm
	context = {
	'Categoryform':form
	}
	if form.is_valid():
		form.save()
		return redirect('post:create')
	return render(request,'snippets/add_category.html',context)
