from rest_framework import serializers
from django.contrib.auth.models import User
from blog_listing.models import MyImage
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

# Serializers define the API representation.


# ==========================================================================
# Serializer for SignUp
# ==========================================================================
class SignUpSerializer(serializers.ModelSerializer):
    # Fields for POST Validation - these should mentioned also in Meta - fields
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:  # Fields for CRUD operations
        model = User
        fields = [
            "email",
            "username",
            "password",
        ]

    def validate(self, attrs):  # to check user already available or not
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):  # to store hash password in database
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        # token = Token.objects.create(user=user)
        # print(token.key)
        return user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class MyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImage
        fields = ["id", "image"]
