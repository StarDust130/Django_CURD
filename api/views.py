from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer


@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello world'})

#! GET ALL /api/products
@api_view(['GET' , "POST"])
def product_list(request):
    pass


def product_detail(request):
    pass

