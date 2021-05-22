from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ExamineForm, FinalTestForm
from . models import Examine, FinalTest

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

@login_required
def examine(request):

	record = Examine.objects.all().filter(Name = request.user.get_username())
	final_record = FinalTest.objects.all().filter(Name = request.user.get_username())

	if request.method == 'POST':
		form = ExamineForm(request.POST)
		
		if form.is_valid():
			form.save()
			Name = form.cleaned_data.get('Name')
			temperature = request.POST.get('temperature')
			dry_cough = form.cleaned_data.get('dry_cough')
			taste = form.cleaned_data.get('taste')
			breathless = form.cleaned_data.get('breathless')
			
			if(int(temperature) <= 38 and dry_cough == False and taste == False
					and breathless == False):
				if len(record) > 0:
					record[0].delete()
				messages.success(request, f'You seem absolutely fine! Come back later and take a test if you feel unwell.')	
				return redirect('examine')		

			return redirect('examine')
	else:	
		form = ExamineForm()

	if request.method == 'POST':
		form_final = FinalTestForm(request.POST)
		
		if form_final.is_valid():
			form_final.save()
			Name = form_final.cleaned_data.get('Name')
			test_result = request.POST.get('test_result')

			if test_result == 'Negative':
				messages.success(request, f'You seem absolutely fine! Come back later and take a test if you feel unwell.')
				return redirect('test')
				
			return redirect('recovery')
	else:	
		form_final = FinalTestForm()	

	if len(final_record) > 0:
		return redirect('recovery')

	return render(request, 'covidcombatapp/examine.html', { 'form': form, 
															'form_final':form_final, 
															'record':record })

@login_required
def test(request):

	record = Examine.objects.all().filter(Name = request.user.get_username())
	final_record = FinalTest.objects.all().filter(Name = request.user.get_username())

	if len(record) > 0:
		record[0].delete()

	if len(final_record) > 0:
		final_record[0].delete()	
	
	if request.method == 'POST':
		form = ExamineForm(request.POST)
		
		if form.is_valid():
			form.save()
			Name = form.cleaned_data.get('Name')
			return redirect('examine')
	else:	
		form = ExamineForm()
	return render(request, 'covidcombatapp/examine.html', { 'form': form })

@login_required
def recovery(request):

	final_record = FinalTest.objects.all().filter(Name = request.user.get_username())

	return render(request, 'covidcombatapp/recovery.html', { 'final_record': final_record })

def vaccination(request):
	
	return render(request, 'covidcombatapp/vaccination.html')	