from django.http import HttpResponseRedirect
from django.urls import reverse 
from django import forms
from django.shortcuts import render


# tasks = ["Go to School", "Wash Plate", "Study"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "Add Item")

# Create your views here.
def index(request):
    # Cecking if tasks is in the session, this is so to create new list every time a different user tries to login 
    if "tasks" not in request.session:
        # created specific session to be equal to an empty list 
        request.session["tasks"] = []
    return render(request, "HTML3/index.html", {
        # "tasks" : tasks
        # render session task which is a list
        "tasks" : request.session["tasks"]
    } )

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST) #this creates a new form inside the variable with all the information from the form submitted,  "request.POST" here would contail all the information submited with the form when
        if form.is_valid():
            task = form.cleaned_data["task"] # Recall inside the from there was an input fiels called "task" then ths function cleans the data, and saves it in a variable called task
            # tasks.append(task)
            # instead of appending to a global list we add to the session list
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index")) # this is to redirct the users back to the index page after succesfully adding the item to the list 
        else:
            return render(request, "HTML3/add.html", {
                "form" : form # here the form already filled is returnd back to the user to see fault or why is is not valid 
            }) 
    return render(request, "HTML3/add.html", {
        "form" : NewTaskForm()
    })
