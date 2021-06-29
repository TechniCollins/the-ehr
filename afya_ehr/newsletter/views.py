from django.shortcuts import render, HttpResponse
from .models import Email

def mailingList(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		Email.objects.get_or_create(email=email)

		return HttpResponse('Your email has been added to our newsletter.')

	return render(request, 'newsletter/comingsoon.html')
