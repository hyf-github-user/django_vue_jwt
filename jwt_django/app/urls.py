# coding:utf-8
# 作者：我只是代码的搬运工
# 文件名  :urls.py
# 时间    :2022/1/26 23:26
from django.conf.urls import url
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegViewSet, StudentViewSet, TestView

urlpatterns = [
    url(r"token/", TokenObtainPairView.as_view(), name="jwt_token"),
    url(r"token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    url(r"^test/$", TestView.as_view(), name="test"),
]

router = routers.DefaultRouter()
# 注册用户视图
router.register(r'users', UserRegViewSet, basename='user_register')
router.register(r'student', StudentViewSet, basename='student')
urlpatterns += router.urls
