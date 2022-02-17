from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, views
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Student
from .serializers import UserRegSerializer, UserInfoSerializer, TokenBaseSerializer

# 继承Django的用户表
User = get_user_model()


class TokenBaseView(TokenObtainPairView):
    """
    重写token的视图
    """
    serializer_class = TokenBaseSerializer


class UserRegViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    注册视图
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    # 权限的选择
    authentication_classes = ()
    # 使用什么进行认证
    permission_classes = ()


class StudentViewSet(views.APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = [authentication.JWTAuthentication]
    # # # 权限的选择
    # # authentication_classes = ()
    # # # 使用什么进行认证
    # # permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = Student

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(name='hyf')
        return Response("查询成功!", status=200)

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        sex = request.data.get('sex')
        sid = request.data.get('sid')
        student = Student(name=name, sex=sex, sid=sid)
        student.save()
        return student


class UserInfoView(RetrieveAPIView):
    """
    获取用户身份权限信息的接口
    """
    serializer_class = UserInfoSerializer
    # 用户必须登录
    permission_classes = (IsAuthenticated,)
    # jwt认证方式
    authentication_classes = [authentication.JWTAuthentication]

    # 获取当前已经登录用户信息  传入
    def get_object(self):
        return self.request.user


class TestView(views.APIView):
    """
    测试接口
    """

    def get(self, request):
        return Response('This is Index Page!', status=200)
