from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from categories.models import Category
from search.models import Tag
from myblog.utils import unique_slug_generator

User =get_user_model()

class Post(models.Model):
	title		=	models.CharField(max_length = 200)
	slug		=	models.SlugField(unique =True, blank = True)
	body		=	models.TextField()
	author		=	models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	featured	=	models.BooleanField(default =False)
	active		=	models.BooleanField(default=True)
	updated		=	models.DateTimeField(auto_now=True)
	published	=	models.DateTimeField(auto_now_add=True)
	category 	=	models.ForeignKey(Category,default=None,on_delete=models.CASCADE)
	tags 	 	=	models.ManyToManyField(Tag,blank =True,related_name='tags')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post:post_detail',kwargs={'slug':self.slug})



def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver,sender=Post)
