from django import forms
from django.forms.widgets import EmailInput,TextInput
from django.contrib.auth import get_user_model
from .models import AuthorProfile

User = get_user_model()
class AuthorForm(forms.ModelForm):
	class Meta:
		model = AuthorProfile
		fields = ('image','title','description')
		widgets = {
					'title': TextInput(
						attrs = {
							'class':'form-control',
							'placeholder':'Your title'
						}
					),
					'description':TextInput(
						attrs = {
							'class':'form-control',
							'placeholder':'Description'
						}
					)
					}

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields =('full_name',)
		widgets = {
					'full_name':TextInput(
						attrs = {
							'class':'form-control',
							'placeholder':'Your Full Name'
						}
					)
					}