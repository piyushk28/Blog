from django import forms
from django.forms.widgets import TextInput

from .models import AuthorProfile

class AuthorForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AuthorForm,self).__init__(*args,**kwargs)
		my_user =self.instance
		name = my_user.author.full_name
		self.field['full_name'].initial=name
	class Meta:
		model = AuthorProfile
		fields = ('title','description','image')