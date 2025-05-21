from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status


@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello world'})

#! GET ALL and CREATE


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():  # ✅ Always check this
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       



#! GET ONE, EDIT and DELETE 
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request):
    pass

