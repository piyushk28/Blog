from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager )

class UserManager(BaseUserManager):
	# Creating User
	def create_user(self,email,full_name,password=None, is_staff=False,is_active=True): #must need 'required fields' as Arguments
		if not email:
			raise ValueError("Users must have an Email Address")

		if not password:
			raise ValueError("User must have a Password")

		if not full_name:
			raise ValueError("User must have a Full  Name")
		user_obj = self.model(
				email = self.normalize_email(email),
				full_name = full_name
			)
		user_obj.set_password(password) # Set or change User Password
		user_obj.admin= is_staff
		user_obj.active= is_active
		user_obj.save(using = self._db)
		return user_obj	

		# Creating super-user
	def create_superuser(self,email,full_name,password=None):
		user = self.create_user(
				email,
				full_name,
				password=password,
				is_staff=True
		)
		return user


class User(AbstractBaseUser):
	email 		= models.EmailField(max_length=255,unique=True)
	full_name 	= models.CharField(max_length=255,blank = True,null=True)
	active		= models.BooleanField(default= True) # Can Login pr Not?
	admin		= models.BooleanField(default=False) # Superuser
	timestamp	= models.DateTimeField(auto_now_add=True)


	USERNAME_FIELD  = 'email'
	# USERNAME_FIELD and passwords are required by default

	REQUIRED_FIELDS = ['full_name']


	objects = UserManager()




	def __str__(self):
		return self.email


	def get_full_name(self):
		if self.full_name:
			return self.full_name
		return self.email

	def get_short_name(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return True

	def has_module_perms(self,app_label):
		return True	


	@property
	def is_staff(self):
		return self.admin

	@property
	def is_active(self):
		return self.active

