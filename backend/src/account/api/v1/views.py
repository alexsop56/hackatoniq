from django.shortcuts import render

# Create your views here.
# account/views.py

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Регистрация нового пользователя",
        responses={201: 'User successfully registered'},
        request_body=RegisterSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ObtainAuthTokenView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)
