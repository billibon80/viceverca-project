#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	length_text = len(user_text.split())
	reversed_text = user_text
	return render(request, 'reverse.html', 
					{'usertext': user_text,
					 'reversed_text': reversed_text,
					 'length_text': length_text
					 })