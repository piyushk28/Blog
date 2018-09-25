from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import AuthorProfile
from .forms import AuthorForm, UserForm


@login_required()
def author_edit_view(request):
	user_form = UserForm(request.POST or None, instance=request.user)
	profile_form = AuthorForm(request.POST or None, instance=request.user.authorProfile)
	if user_form.is_valid() and profile_form.is_valid():
		user_form.save()
		profile_form.save()
		# messages.success(request, ('Your profile was successfully updated!'))
		return redirect('authorProfile:profile')
	else:
		# messages.error(request, ('Please correct the error below.'))
		pass
	return render(request, 'authorprofile/editProfile.html', {
	'user_form': user_form,
	'profile_form': profile_form
	})


class AuthorDetailView(LoginRequiredMixin,TemplateView):
	template_name = 'authorprofile/author_detail.html'
	def get_context_data(self, **kwargs):
		context = super(AuthorDetailView, self).get_context_data(**kwargs)
		user = self.request.user
		try:
			instance = AuthorProfile.objects.get(author=user)
		except AuthorProfile.DoesNotExist:
			return http404('Profile Not found ')
		except Product.MultipleObjectsReturned:
			qs=AuthorProfile.objects.filter(author=user)
			instance =qs.first()
		if instance.title is '' or instance.description is '' or user.full_name is '' :
			info = 'Please navigate to <a href={edit}>EditProfile</a> and fill your details.'.format(edit=reverse_lazy('authorProfile:edit_author'))
			print("yo")
		else:
			info = ''
			print("yoyooo")
		context ={
		'instance':instance,
		'full_name':user.full_name,
		'email': user.email,
		'info':info
		}
		return context