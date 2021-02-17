from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    #template = "home.html"
    #context = {}
    #return HttpResponse("<h1> Hello World </h1>")
    my_title = " KSP ASTUNGKARA MESARI "
    context = {"title":my_title}
    return render(request, "home.html", context )

def about(request):
    return render(request, "about.html", {"title":"about"})

def contact(request):
    return render(request, "contact.html", {"title":"contact"})