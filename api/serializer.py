#Api serializer

from rest_framework import serializers
from Shop.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'image', 'category',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']