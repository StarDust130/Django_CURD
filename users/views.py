
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

#! Create User 👺


class UserCreateView(APIView):
    permission_classes = [AllowAny]  # Anyone can create an account

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User created successfully 🥳",
                    "user": serializer.data  # send back created user data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! Login 💠


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return Response({"message": "Login successful 🥳"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password 😢"}, status=status.HTTP_401_UNAUTHORIZED)
