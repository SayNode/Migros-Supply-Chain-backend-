from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','category_name']


class CategorySerializerID(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']

