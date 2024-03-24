from django import forms
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ["name", "instructions", "is_private",
                  "prep_time", "cook_time", "difficulty"]
