from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index" ),
    path('<str:name>', views.name, name= "name"),
    path("allen", views.allen, name="allen")
]