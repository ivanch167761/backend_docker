from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [ 
            '/api/products',
            'api/products/<id>/'            
            ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

def index(request):
    return render(request, "build/index.html")

