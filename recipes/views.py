from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RecipeSerializer
from .models import Recipe


# Create your views here.
#This is an example I found of how to create and index view will improve soon.
# It isn't ideal to use csrf_exempt in this case. Potentially need to use some sort of cors library.
@csrf_exempt
@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        # Review what serializer methods are available for learning purposes.
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['PUT','GET'])
def recipe(request, pk):
    try:
        recipe = get_object_or_404(Recipe, id=pk)
    except Recipe.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['user'])
        #user.set_password here takes the password param and creates a hash to be store in the db wether than the plain text version above.
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Figure out a better way to user token based authentication. Something feels a bit off about this way.
# However, it is permissiable for the sake of learning.
@api_view(['POST'])
def login(request):
    '''
        Research more in how django handles retrieveing from requests. The example I am using with setting variables comes from
        https://docs.djangoproject.com/en/5.0/topics/auth/default/#how-to-log-a-user-in
        However other examples other examples I have come across use the syntax request.data['information']
    '''
    email = request.POST['email']
    password = request.POST['password']
    user = get_object_or_404(User,email=email)
    # user.check_password is a method that checks the request password against the hashed password in the database. 
    if user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response("missing user", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_token(request):
    return Response("Signed in!",status=status.HTTP_200_OK)
