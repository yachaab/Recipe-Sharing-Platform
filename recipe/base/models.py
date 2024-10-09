from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Category Model: Fields like name and slug.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
# Recipe Model: Fields like title, ingredients, instructions, category (ForeignKey), author (ForeignKey to User), image, created_at, updated_at.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    ingredients = models.TextField(max_length=6000)
    instructions = models.TextField(max_length=6000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100)
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    
    def __str__(self):
        return self.title

# Comment Model: Fields like recipe (ForeignKey), author (ForeignKey to User), content, created_at.
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content