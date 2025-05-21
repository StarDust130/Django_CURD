from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # Password should be write-only: you can send it to create or update,
    # but it will never be sent back in API responses (security!)
    password = serializers.CharField(
        write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        # Only expose fields you want in API responses (not all fields)
        fields = ['id', 'username', 'email',
                  'password', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': True},  # Make email required
        }

    #! When User Create Account 😊 
    def create(self, validated_data):
        # Use the built-in method to create user and hash password properly
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user
    #! When User Update Account 😆
    def update(self, instance, validated_data):
        # Handle updating user data and password safely
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # This hashes the password!

        instance.save()
        return instance
