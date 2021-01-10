"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    a2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
设置每一个URL的网址要对应的函数以及对应的方式
是创建新的网页时新编辑的文件！！！

"""

from django.contrib import admin
from django.urls import path
"""asfdfdsaf"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
