from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	context_dict = {'boldmessage': 'I am bold form from the context.'}
	return render(request, 'rango/index.html', context_dict)


def abt(request):
	context_dic = {'myName': 'Sniper'}
	return render(request,'rango/about.html',context_dic)