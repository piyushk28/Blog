from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

    def clean_title(self):
    	title = self.cleaned_data.get('title')
    	qs = Category.objects.filter(title__exact = title)
    	if qs.exist():
    		raise forms.ValidationError("'{{t}}' named category already exist, Please add a New Category".format(t=title))
    	return title	