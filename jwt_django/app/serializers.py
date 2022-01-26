# coding:utf-8
# 作者：我只是代码的搬运工
# 文件名  :serializers.py
# 时间    :2022/1/26 23:37
from django.contrib.auth import get_user_model
from rest_framework import serializers

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
