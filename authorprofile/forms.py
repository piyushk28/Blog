from django import forms
from django.forms.widgets import EmailInput,TextInput
from django.contrib.auth import get_user_model
from .models import AuthorProfile

User = get_user_model()
class AuthorForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['title'].required=True
		self.fields['description'].required=True


	class Meta:
		model = AuthorProfile
		fields = ('image','title','description')
		widgets = {
					'title': TextInput(
						attrs = {
							'class':'form-control author-title',
							'placeholder':'Your title'
						}
					),
					'description':TextInput(
						attrs = {
							'class':'form-control author-description',
							'placeholder':'Description'
						}
					)
					}

class UserForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['full_name'].required=True

	class Meta:
		model=User
		fields =('full_name',)
		widgets = {
					'full_name':TextInput(
						attrs = {
							'class':'form-control full-name',
							'placeholder':'Your Full Name'
						}
					)
					}
