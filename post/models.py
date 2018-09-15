from django.db import models
from django.db.models.signals import pre_save

from categories.models import Category
from myblog.utils import unique_slug_generator

class Post(models.Model):
	title		=	models.CharField(max_length = 200)
	slug		=	models.SlugField(unique =True, blank = True)
	body		=	models.TextField()
	author		=	models.CharField(max_length = 40)
	featured	=	models.BooleanField(default =False)
	active		=	models.BooleanField(default=True)
	updated		=	models.DateTimeField(auto_now=True)
	published	=	models.DateTimeField(auto_now_add=True)
	category 	=	models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/{slug}/".format(slug=self.slug)



def post_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(post_pre_save_receiver,sender=Post)