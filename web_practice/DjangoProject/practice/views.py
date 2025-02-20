import json


from practice.service import UserInfoServicesimple
from django.shortcuts import HttpResponse,render
from django.http.response import HttpResponseBase, JsonResponse

def check_page(page:int):
    if page <= 0:
        raise ValueError('page 必须大于0')
    return int(page)

def check_size(size:int):
    if size <= 0:
        raise ValueError('size 必须大于0')
    return int(size)

# Create your views here.
class UserInfoViewSimple():
    def get(self,request):
        query_parms = request.GET

        #获取查询参数
        name = query_parms.get('name')
        account = query_parms.get('account')
        page = query_parms.get('page')
        size = query_parms.get('size')

        #数据校验
        check_data = {
            'name':name,
            'account':account,
            'page':check_page(page),
            'size':check_size(size)
        }

        result = UserInfoServicesimple.query_info(check_data)
        data = {
            'code':'200',
            'meg':'ok',
            'data':result
        }
        return JsonResponse(data)

    def post(self,request):
        pass


def test(request):

    return HttpResponse(json.dumps({"msg": "ok"}))
