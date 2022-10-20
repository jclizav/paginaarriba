from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse



# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def blog(request):
    return render(request, "core/blog.html")

def contacto(request):
    return render(request, "core/contacto.html")             

#def about(request):
 #   return HttpResponse(html_base + """<h1> Mi página</h1><h2>Hola yo soy jc</h2><p>mi texto</p>""")    