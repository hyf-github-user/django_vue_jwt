"""jwt_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls

from app.views import UserInfoView, TokenBaseView

schema_view = get_schema_view(
    openapi.Info(title="swaggerAPI文档",
                 default_version="v1",
                 description="API文档",
                 terms_of_service="",
                 contact=openapi.Contact(email="1348977728@qq.com"),
                 license=openapi.License(name="MIT")),
    public=True,
    authentication_classes=(),
    permission_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置总路由
    path('jwt/', include('app.urls')),
    # 登录路由
    url(r"user/login", TokenBaseView.as_view(), name="user_login"),
    # 获取身份路由
    url(r"user/info", UserInfoView.as_view(), name="user_info"),
    # drf内置API文档
    url(r"docs/", include_docs_urls(title="drf内置的api文档")),
    # 配置swagger的配置
    url(r"swagger/", schema_view.with_ui("swagger",
                                         cache_timeout=0), name="schema-swagger"),
    url(r"redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
