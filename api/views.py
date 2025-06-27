#api view
from api.serializer import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Shop.models import Product, Category

class ProductListView(APIView):
    """
    API view to retrieve a list of products.
    """
    def get(self, request):
        """
        Handle GET requests to retrieve all products.
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryListView(APIView):
    """
    API view to retrieve a list of categories.
    """
    def get(self, request):
        """
        Handle GET requests to retrieve all categories.
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    

