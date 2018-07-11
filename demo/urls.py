"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #将users的所有路由都包含进来
    # url(r'^users/', include('users.urls')),
    #路由可以不用子应用定义
    # url(r"^users/index/$",views.index),
    #路由命名空间，辅助reverse实现反向解析
    url(r"^users/",include('users.urls',namespace='users')),
    #演示请求和响应
    url(r"^",include('request_response.urls')),
    url(r'^',include('responsetext.urls')),
    url(r"^",include('classview.urls')),

]
