from distutils.command.register import register
from http.client import responses

from django.http import JsonResponse
from django.shortcuts import render , HttpResponse
from django.http.request import HttpRequest
from django.views import View

from practice.service import UserInfoService

# Create your views here.
class UserInfoView():
    def get(self,request):
        return render(request,'UserInformation.html')

    def post(self,request):
        user_name = request.POST.get('user_name')
        user_account = request.POST.get('user_account')
        search_information = {'user_name':user_name,'user_account':user_account}
        user_info = UserInfoService.query_info(search_information)

        return user_info