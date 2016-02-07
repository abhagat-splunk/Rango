from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	context_dict = {'boldmessage': 'I am bold form from the context.'}
	return render(request, 'rango/index.html', context_dict)


def abt(request):
	return HttpResponse("Rango says this is the about page. <br/> <a href='/rango/'>Go back to Main Page!</a>")