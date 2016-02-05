from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Rango says hey hello world!  <br/> <a href='/rango/about'>About</a>")

def abt(request):
	return HttpResponse("Rango says this is the about page. <br/> <a href='/rango/'>Go back to Main Page!</a>")