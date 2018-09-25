from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth import get_user_model

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','tags','featured','active','body',)
    def save(self, commit=True ,*args, **kwargs):
               request = None
               request = kwargs.pop('request')
               m = super(PostCreateForm, self).save(commit=False, *args, **kwargs)
               if m.author is None and request is not None:
                   print(request.user)
                   m.author= request.user
                   m.save()