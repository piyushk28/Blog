from django import template

from post.models import Post
from categories.models import Category

register = template.Library()

# This custom tag render Category_list on base.html  

@register.inclusion_tag('snippets/category_list.html')
def category_list():
	list = Category.objects.all()
	# print(list)
	return{"list":list}