from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models  import User


class RecipeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Recipe
        fields = ('id', 'name', 'instructions', 'is_private', 'prep_time', 'cook_time',
                  'difficulty', 'servings')

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id','username', 'password', 'email')