from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework import status, views
from rest_framework.response import Response
import logging

from .serializers import TokenObtainPairSerializer, RegisterSerializer
from .services import LoginSevices
from user.models import User

class TokenObtainPairAPIView(TokenObtainPairView):
    """ログイン認証を行うAPIクラス"""

    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer

class RegisiterAPIView(generics.CreateAPIView):
    """ユーザー登録を行APIクラス"""

    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer







