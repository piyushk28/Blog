from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
from categories.models import Category
from myblog.utils import unique_slug_generator

User =get_user_model()

class Post(models.Model):
	title		=	models.CharField(max_length = 200)
	slug		=	models.SlugField(unique =True, blank = True)
	body		=	models.TextField()
	author		=	models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
	featured	=	models.BooleanField(default =False)
	active		=	models.BooleanField(default=True)
	updated		=	models.DateTimeField(auto_now=True)
	published	=	models.DateTimeField(auto_now_add=True)
	category 	=	models.ForeignKey(Category,default=None,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post:post_detail',kwargs={'slug':self.slug})



def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	# if not instance.author :
	# 	instance.author=User
pre_save.connect(pre_save_receiver,sender=Post)

# def post_save_receiver(sender,created,instance,*args,**kwargs):
	
# post_save.connect(post_save_receiver,sender=Post)