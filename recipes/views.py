from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import RecipeSerializer
from rest_framework import  viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Recipe


# Create your views here.
class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class AuthenticationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content ={
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)