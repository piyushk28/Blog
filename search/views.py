from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from post.models import Post

class SearchPostView(ListView):
	template_name='search/view.html'

	def get_context_data(self,*args,**kwargs):
		context = super(SearchPostView,self).get_context_data(*args,**kwargs)
		query=self.request.GET.get('q')	
		context['query']=query
		return context
	def get_queryset(self,*args,**kwargs):
		request=self.request
		print(request.GET)
		query=request.GET.get('q',None)
		if query is not None:
			qs = Post.objects.filter(Q(title__icontains=query) |
										Q(body__icontains=query) |
										Q(category__title__icontains=query) |
										Q(tags__title__icontains=query))
			print(qs)
			return qs
		return Post.objects.filter(featured=True)
