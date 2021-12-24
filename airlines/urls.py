from django.urls import path
from . import views

urlpatterns = [
    path("", views.search),
    path("search_result", views.search_result, name="search_result")
]