from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    @action(detail=False, methods=['GET'])
    def list_recipe_by_catregory(self, request):
        query_string = request.GET.get('category', None)
        queryset_id = Category.objects.filter(name=query_string).values('id')
        print('queryset_id: ', queryset_id)
        if queryset_id.exists():
            category_id = queryset_id.first()['id']
            queryset = self.queryset.filter(category=category_id).values('title', 'ingredients', 'instructions', 'image')
            return Response(queryset)
        else:
            return Response({'error': 'category not found'}, status=404)
    
    @action(detail=False, methods=['GET'])
    def search_by_title_or_ingredients(self, request):
        """
        Search using query strings
        """
        query_string_title = request.GET.get('title')
        query_string_ingri = request.GET.get('ingri')
        print('title: ', query_string_title)
        print('ingri: ', query_string_ingri)
        if query_string_title:
            title_queryset = self.queryset.filter(title__contains=query_string_title).values('title', 'ingredients', 'instructions', 'image')
            print('title queryset: ', title_queryset)
            if title_queryset:
                return Response(title_queryset)
        if query_string_ingri:
           ingri_queryset = self.queryset.filter(ingredients__contains=query_string_ingri).values('title', 'ingredients', 'instructions', 'image')
           if ingri_queryset:
               return Response(ingri_queryset)
        return Response({'error': 'result not found'}, status=404)
    
    @action(detail=False, methods=['POST'])
    def search(self, request):
        print('data: ', request.data)
        return Response({})
    
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer