from django.shortcuts import render
import datetime

# Create your views here.
# def index(request):
#     now = datetime.datetime.now() 
#     if now.month and now.day == 1:
#         return render(request, "HTML/yes.html")
#     else:
#         return render(request, "HTML/no.html")

def index(request):
    now = datetime.datetime.now()
    return render(request, "HTML/newyear.html", {
        "answer": now.month and now.day == 1
    })
