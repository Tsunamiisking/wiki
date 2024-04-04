from django.urls import path
from . import views

# Adding a "app_name" to this file help with url identification to help specify the name when
# linking pages with the "{% url '<urlpatternsname>'%}" format in the HTML page
# app_name = "<specific name to identify for this specific app>"
# then {% url '<specific name to identify for this specific app>:<name>'%}
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]