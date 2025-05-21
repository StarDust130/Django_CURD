
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

#! Create User 👺
class UserCreateView(APIView):
    permission_classes = [AllowAny]  # Anyone can create account

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! Login 💠
class LoginView(APIView):
    permission_classes = [AllowAny]  # Anyone can try to login

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
