from django.urls import re_path,path
from . import  views

app_name="recipes"
urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('get_token', views.get_token),
    re_path('recipes', views.recipes),
    path('recipe/<int:pk>/', views.recipe)
]