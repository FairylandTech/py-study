from django.shortcuts import render

# Create your views here.

from django.http.request import HttpRequest
from django.http.response import HttpResponseBase, JsonResponse

from fairylandfuture.structures.builder.db import StructureMySQLExecute
from utils.db import dbtools


def test(request: HttpRequest) -> HttpResponseBase:
    if request.method == "GET":
        print("测试请求")

        sql = "select id, name, account, department, created_at, updated_at, existed from example_user_info_1 where id = %(id)s;"
        params = {"id": 1}
        result = dbtools.select(StructureMySQLExecute(sql, params))
        print(result)
        data = {
            "code": 200,
            "message": "OK",
            "data": None if result is True else result
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"msg": "不支持的请求方式!"})
