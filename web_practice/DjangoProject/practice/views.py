import json

from practice.service import UserInfoService
from django.shortcuts import HttpResponse,render


# Create your views here.
class UserInfoView():
    def get(self,request):
        return render(request,'UserInformation.html')

    def post(self,request):
        name = request.GET.get('name')
        account = request.GET.get('account')
        page = request.GET.get('page')
        size = request.GET.get('size')


        
        user_info = UserInfoService.query_info()

        return user_info







def test(request):
    return HttpResponse(json.dumps({"msg": "ok"}))
