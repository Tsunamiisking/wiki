from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "HTML/index.html")

def name(request, name):
    return render(request, "HTML/greeting.html", {
        "name": name.capitalize()
    })

def allen(request):
    return HttpResponse("Hello Allen!")