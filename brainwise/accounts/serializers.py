# from rest_framework import serializers
# from .models import UserAccount

# class UserAccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAccount
#         fields = '__all__'
# accounts/serializers.py
from rest_framework import serializers
from .models import UserAccount
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # You can hash the password here, or Django's built-in user manager will handle it when saving
        user = UserAccount.objects.create(**validated_data)
        return user


class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")
        print(user.password, password, check_password(password, user.password))
        if not check_password(password, user.password):  # In a real app, you'd use Django's `check_password` method here
            raise serializers.ValidationError("Invalid username or password")

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
