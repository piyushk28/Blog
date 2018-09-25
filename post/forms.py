from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth import get_user_model

from .models import Post

class PostCreateForm(forms.ModelForm):
  title = forms.CharField(label = 'Title',widget = forms.TextInput(
                          attrs = {
                            'class':'form-control',
                            'placeholder':"Enter Post Title."
                          }
                          ) 
          )
  body = forms.CharField(label='Post Body',widget=forms.TextInput(
                          attrs = {
                            'class':'form-control',
                            'placeholder':"Enter Post Body."
                          }
                          )
         )

  active = forms.BooleanField(label= 'Acitve',widget=forms.CheckboxInput(
                            attrs={
                            'class':'form-control',
                            }
                            )
  )
  class Meta:
    model = Post
    fields = ('title','category','tags','active','body',)

  def save(self, commit=True ,*args, **kwargs):
    request = kwargs.get('request',None)
    m = super(PostCreateForm, self).save(commit=False, *args, **kwargs)
    if m.author is None and request is not None:
      print(request.user)
      m.author= request.user
      m.save()

class PostEditForm(forms.ModelForm):

  title = forms.CharField(label = 'Title',widget = forms.TextInput(
                          attrs = {
                            'class':'form-control',
                            'placeholder':"Enter Post Title."
                          }
                          ) 
          )
  body = forms.CharField(label='Post Body',widget=forms.TextInput(
                          attrs = {
                            'class':'form-control',
                            'placeholder':"Enter Post Body."
                          }
                          )
         )
  active = forms.BooleanField(label= 'Active',widget=forms.CheckboxInput(
                            attrs={
                            'class':'form-control'
                            }
                            )
  )
  class Meta:
    model =Post
    fields = ('title','tags','active','body',)

