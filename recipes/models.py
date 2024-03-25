from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    is_private = models.BooleanField(default=False)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    difficulty = models.CharField(max_length=50)
    servings = models.IntegerField()
    comments_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Category(models.Model):
    name = models.TextField(max_length=100)
