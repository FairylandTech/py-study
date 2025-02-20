# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-18 20:56:59 UTC+08:00
"""

from django.urls import path

from app.views import test
from app.views import UserInfoAPIView

urlpatterns = [
    path(r"/test", test),
    path(r"/user", UserInfoAPIView.as_view()),
]
