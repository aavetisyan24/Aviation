from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('airlines/', views.airlines, name="blog-airlines"),
    path('flyto/', views.flyto, name="blog-flyto"),
    path('about/', views.about, name="blog-about"),

]