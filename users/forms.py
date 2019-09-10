from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

	email = forms.EmailField()
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=60)

	def __init__(self, *args, **kwargs):                                 #ypoxreotika pedia symplyrwshs
	    super(UserRegisterForm, self).__init__(*args, **kwargs)
	    self.fields['first_name'].required = True
	    self.fields['last_name'].required = True



	class Meta:
	    model = User
	    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']