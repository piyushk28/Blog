from django.shortcuts import render
from .forms import AuthorForm
from django.views.generic import CreateView

# Create your views here.

class AuthorEditView(CreateView):
	form_class = AuthorForm
	template_name = 'authorprofile/editProfile.html'
	success_url = '/'
