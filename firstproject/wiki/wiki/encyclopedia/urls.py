from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entriesroute, name="entriesroute"),
    path("", views.index, name="search"),
    path("create", views.create, name="create"),
    path("random", views.randomPage, name="randomPage"),
    path("edit", views.editentries, name="editentries")
]
