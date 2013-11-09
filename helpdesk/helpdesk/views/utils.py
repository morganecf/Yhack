from django.contrib.auth.models import User

'''
Some utility functions useful for views.
'''

mcgill_email = "mail.mcgill.ca"
mcgill_email_prof = "mcgill.ca"

def isValidEmail(email):
	return email.endswith(mcgill_email) or email.endswith(mcgill_email_prof)

def email_exists(email):
	return User.objects.filter(email = email).count() > 0