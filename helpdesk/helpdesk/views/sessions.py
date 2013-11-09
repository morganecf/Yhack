
#import backends.base.SessionBase
from django.contrib.auth.models import User

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from smtplib import SMTPException
from helpdesk.settings import EMAIL_HOST_USER

from utils import valid_email, email_exists

'''
Views that have to do with user sessions. 
'''

#EMAIL_HOST_USER = "cloudhelpyhack@gmail.com"

def login(request):
	pass

def logout(request):
	pass

def signup(request):
	context = {}
	isVal = False 		# UGH SO INELEGANT 
	exists = False 		# UGH AGAIN
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']

		exists = email_exists(email)
		if exists:
			context["failure_message"] = "Email already exists."
			return render(request, 'home.html', context)
		isVal = valid_email(email)

		if isVal:
			subject = "Welcome to CloudHelp!"
			message = "Hello " + first_name + " " + last_name + "! Thanks for joining CloudHelp."

			try:
				send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently=False)
				username = first_name + " " + last_name
				user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
				user.save()
				return HttpResponseRedirect('/userhome/')
			except SMTPException:
				return HttpResponseRedirect('/failure/')

		else:
			context["failure_message"] = "Invalid email."
			return render(request, 'home.html', context) 
	
	return render(request, 'home.html', context)

