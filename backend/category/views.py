from django.shortcuts import render

# Create your views here.

from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import Category
from .serializers import CategorySerializer


# Chapter views
class ListCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class CreateCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class SearchCategoryByStringAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']



class RetrieveUpdateDestroyCategoryByID(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('pk')
    serializer_class = CategorySerializer
    permission_classes = []
    lookup_field = 'id'





