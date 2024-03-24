from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.Serializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'instructions', 'is_private', 'prep_time', 'cook_time',
                  'difficulty', 'servings')
