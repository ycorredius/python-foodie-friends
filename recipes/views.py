from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import RecipeSerializer
from rest_framework import viewsets
from .models import Recipe


# Create your views here.
class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


@login_required(login_url="/login")
def newrecipe(request):
    return render(request, "recipes/newrecipe.html")
