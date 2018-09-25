from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from myblog.utils import unique_slug_generator

class Category(models.Model):

	title		= models.CharField(max_length= 40,unique= True)
	slug		= models.SlugField(blank= True,unique= True)
	created		= models.DateTimeField(auto_now= True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category',kwargs={'slug':self.slug})

def category_pre_save_signal(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(category_pre_save_signal, sender= Category)