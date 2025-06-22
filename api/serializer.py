#Api serializer

from rest_framework import serializers
from Shop.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'image', 'category',]