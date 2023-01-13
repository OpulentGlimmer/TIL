# Master urls.py
"""one_to_many URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 방문자가 articles/ 로 접속할 때는 board 앱 폴더의 urls.py를 참조하기 위해 include를 쓴다.
    path('articles/', include('board.urls')),
    # 방문자가 accounts/ 로 접속할 때는 accounts 앱 폴더의 urls.py를 참조하기 위해 include를 쓴다.
    path('accounts/', include('accounts.urls')),
    # articles/1/
    # articles/
    # articles/create
]
