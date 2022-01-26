from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户系统,扩展django自带的user表
    """
    # 身份
    LEVEL = (
        ('1', '超级管理员'),
        ('2', '协管员'),
        ('3', '普通用户'),
    )
    name = models.CharField(max_length=32, blank=True, verbose_name="用户名")
    mobile = models.CharField(max_length=11, blank=True, verbose_name="用户电话")
    level = models.CharField(choices=LEVEL, max_length=32, blank=True, verbose_name="用户等级")

    def __str__(self):
        return self.name
