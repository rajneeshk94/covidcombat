from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ExamineForm
from . models import Examine

def home(request):
	return render(request, 'covidcombatapp/home.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now login')
			return redirect('login')
	else:	
		form = UserRegisterForm()
	return render(request, 'covidcombatapp/register.html', { 'form': form })

def examine(request):

	record = Examine.objects.all().filter(Name = request.user.get_username())

	if request.method == 'POST':
		form = ExamineForm(request.POST)
		
		if form.is_valid():
			form.save()
			Name = form.cleaned_data.get('Name')
			return redirect('examine')
	else:	
		form = ExamineForm()
	return render(request, 'covidcombatapp/examine.html', { 'form': form, 'record':record })

def test(request):

	record = Examine.objects.all().filter(Name = request.user.get_username())

	if len(record) > 0:
		record[0].delete()
	
	if request.method == 'POST':
		form = ExamineForm(request.POST)
		
		if form.is_valid():
			form.save()
			Name = form.cleaned_data.get('Name')
			return redirect('examine')
	else:	
		form = ExamineForm()
	return render(request, 'covidcombatapp/examine.html', { 'form': form })		