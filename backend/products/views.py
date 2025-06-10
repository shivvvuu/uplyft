from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def get_products(request):
    search = request.GET.get('search')
    products = Product.objects.all()
    if search:
        products = products.filter(name__icontains=search)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
