from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Examine, FinalTest


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ExamineForm(ModelForm):
	
	class Meta:
		model = Examine
		fields = '__all__'		


class FinalTestForm(ModelForm):
	
	class Meta:
		model = FinalTest
		fields = '__all__'	