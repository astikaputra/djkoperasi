from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #template = "home.html"
    #context = {}
    #return HttpResponse("<h1> Hello World </h1>")
    my_title = " KSP ASTUNGKARA MESARI "
    context = {"title":my_title}
    return render(request, "tabungan.html", context )

