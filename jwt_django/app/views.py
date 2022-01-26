from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from .serializers import UserRegSerializer

User = get_user_model()


class UserRegViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    注册视图
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    # authentication_classes =
