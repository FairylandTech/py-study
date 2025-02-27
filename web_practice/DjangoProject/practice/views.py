import json

from django.db.models.expressions import result
from django.http.request import HttpRequest
from django.shortcuts import HttpResponse,render
from django.http.response import HttpResponseBase, JsonResponse
from django.views import View

from practice.service import UserInfoServicesimple

def check_page(page):
    page = int(page)
    if page <= 0:
        raise ValueError('page 必须大于0')
    return int(page)

def check_size(size):
    size = int(size)
    if size <= 0:
        raise ValueError('size 必须大于0')
    return int(size)

# Create your views here.
class UserInfoViewSimple(View):
    def get(self,request):
        query_parms = request.GET

        #获取查询参数
        name = query_parms.get('name')
        account = query_parms.get('account')
        page = query_parms.get('page',1)
        size = query_parms.get('size',10)

        #数据校验
        check_data = {
            'name':name,
            'account':account,
            'page':check_page(page),
            'size':check_size(size)
        }

        print(f"check_data:{check_data}")

        result = UserInfoServicesimple.query_info(check_data)
        data = {
            'code':'200',
            'meg':'ok',
            'data':result
        }
        print(f"data:{data}")
        return JsonResponse(data)
    #
    # def post(self,request):
    #     pass
    #
    # def add(self,request):
    #     add_params = request.POST
    #
    #     name = add_params.get("name")
    #     account = add_params.get("account")
    #     department = add_params.get("department")
    #     status = add_params.get("status")
    #     create_at =

    def update(self,request):
        query_parms = request.POST

        id = query_parms.get('id')
        name = query_parms.get('name')
        account = query_parms.get('account')
        department = query_parms.get('department')
        status = query_parms.get('staus')
        #数据校验

        updata_parms = {
            'id':id,
            'name':name,
            'account':account,
            'department':department,
            'staus':status
        }
        result = UserInfoServicesimple.updateservice(updata_parms)
        return result




def test(request):

    return HttpResponse(json.dumps({"msg": "ok"}))
