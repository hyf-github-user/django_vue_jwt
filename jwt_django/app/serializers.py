# coding:utf-8
# 作者：我只是代码的搬运工
# 文件名  :serializers.py
# 时间    :2022/1/26 23:37
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Student

# django的user
User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    """
    注册用户时的序列化器
    """

    def create(self, validated_data):
        """
        自定义创建用户方法
        :param validated_data:
        :return:
        """
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'mobile', 'level']


class StudentSerializer(serializers.ModelSerializer):
    """
    学生的序列化器
    """

    class Meta:
        model = Student  # 指定的模型类
        fields = ('pk', 'name', 'sex', 'sid',)  # 需要序列化的属性


class UserInfoSerializer(serializers.ModelSerializer):
    """
    扩展的User的序列化器
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'level']


class TokenBaseSerializer(TokenObtainPairSerializer):
    """
    重写token的序列化器
    """

    def validate(self, attrs):
        """
        重写token返回的结果
        :param attrs:
        :return:
        """
        data = super().validate(attrs)
        data['code'] = 200
        data['message'] = 'success'
        return data
