from django.shortcuts import render, redirect
from .forms import AuthorForm, UserForm
from django.views.generic import CreateView
from .models import AuthorProfile
# Create your views here.

# class AuthorEditView(CreateView):
# 	form_class = AuthorForm
# 	template_name = 'authorprofile/editProfile.html'
# 	success_url = '/'
	
# 	def get_form_kwargs(self):
# 	    kwargs = super(AuthorEditView, self).get_form_kwargs()
# 	    kwargs.update({'user': self.request.user})
# 	    return kwargs


def author_edit_view(request):
	user_form = UserForm(request.POST or None, instance=request.user)
	profile_form = AuthorForm(request.POST or None, instance=request.user.authorProfile)
	if user_form.is_valid() and profile_form.is_valid():
		user_form.save()
		profile_form.save()
		# messages.success(request, ('Your profile was successfully updated!'))
		return redirect('/')
	else:
		# messages.error(request, ('Please correct the error below.'))
		print('error')
	return render(request, 'authorprofile/editProfile.html', {
	'user_form': user_form,
	'profile_form': profile_form
	})
