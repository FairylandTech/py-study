from django.urls import path

from .views import test,UserInfoViewSimple

urlpatterns = [
    path('test/', test),
    path('user_info',UserInfoViewSimple.get)
]