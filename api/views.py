from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, MyImageSerializer
from blog_listing.models import MyImage
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .token import get_tokens_for_user
from rest_framework.permissions import BasePermission
import json
from django.contrib.auth import get_user_model as user
from django.utils.timezone import now


# Create your views here.
# ==========================================================================
# views for signUp
# ==========================================================================
class SignUpView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data
        print(data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "User Created successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request: Request):
    #     post = User.objects.all()
    #     serializer = self.serializer_class(instance=post, many=True)
    #     response = {"message": "User Created successfully", "data": serializer.data}
    #     return Response(data=response, status=status.HTTP_200_OK)


# ==========================================================================
# views for Login
# ==========================================================================
class LoginView(APIView):
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request: Request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        # if user.is_staff == False:
        #     return Response(
        #         data={"Message": "Admin User Only!", "admin": False},
        #         status=status.HTTP_200_OK,
        #     )
        if user is not None:
            # response = {"message": "Login successfully", "token": user.auth_token.key}  #DRF Tokens
            tokens = get_tokens_for_user(user)

            # Update last_login
            user.last_login = now()
            user.save(update_fields=["last_login"])
            response = {"message": "Login successfully", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"Message": "Invalid email or password"}, status=status.HTTP_200_OK
            )

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MyImageViewSet(viewsets.ModelViewSet):
    queryset = MyImage.objects.all()
    serializer_class = MyImageSerializer
