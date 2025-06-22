#api view
from api.serializer import ProductSerializer
from Shop.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        return Response(serializer.data)
    
    def post(self, request):
        """
        Handle POST requests to create a new product.
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

