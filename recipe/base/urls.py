from django.urls import re_path, include
from rest_framework import routers
from .views import RecipeViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'categories', CategoriesViewSet, basename='category')

urlpatterns = [
    re_path('', include(router.urls))
]