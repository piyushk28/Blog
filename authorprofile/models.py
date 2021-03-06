from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

import random
import os

# Create your models here
User = get_user_model()

def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name, ext=os.path.splitext(base_name)
	return name, ext

# To return a  new  path for  image
def upload_image_path(instance,filename):
	new_filename=random.randint(1,2345356465)
	name, ext =  get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return 'author/{new_filename}/{final_filename}'.format(
			new_filename=new_filename,
			final_filename=final_filename
			)


class AuthorProfile(models.Model):
	author 				= models.OneToOneField(User, on_delete=models.CASCADE,related_name='authorProfile')
	title				= models.CharField(max_length=200,blank=True)
	description			= models.TextField(blank=True)
	image				= models.ImageField(upload_to=upload_image_path,blank=True)

	def __str__(self):
		return self.author.email

	def get_full_name(self):
		if self.author.full_name:
			return self.author.full_name
		else:
			return None

def post_save_assign_user(sender,instance,created,*args,**kwargs):
	user_obj = instance
	if created:
		author_obj =AuthorProfile.objects.create(author=user_obj)

post_save.connect(post_save_assign_user,sender=User)

def post_save_user(sender,instance,*args,**kwargs):
	instance.authorProfile.save()
	
post_save.connect(post_save_user,sender=User)