# Create your views here.

from django.http.request import HttpRequest
from django.http.response import HttpResponseBase, JsonResponse
from django.views import View

from fairylandfuture.structures.builder.db import StructureMySQLExecute
from utils.db import dbtools
from fairylandfuture.modules.validator.validators import Validator, RequestParamsValidator

from app.services import UserInfoService


def test(request: HttpRequest) -> HttpResponseBase:
    if request.method == "GET":
        print("测试请求")

        sql = "select id, name, account, department, created_at, updated_at, existed from example_user_info_1 where id = %(id)s;"
        params = {"id": 1}
        result = dbtools.select(StructureMySQLExecute(sql, params))
        print(result)
        data = {"code": 200, "message": "OK", "data": None if result is True else result}
        return JsonResponse(data)
    else:
        return JsonResponse({"msg": "不支持的请求方式!"})


def validata_page(value: int):
    if value <= 0:
        raise ValueError("page参数必须大于0")

    return True


def validata_size(value: int):
    if value <= 0:
        raise ValueError("size参数必须大于0")

    return True


class UserInfoAPIView(View):

    def get(self, request: HttpRequest) -> HttpResponseBase:
        query_params = request.GET

        # 1. 获取前端传来的查询参数
        name = query_params.get("name")
        account = query_params.get("account")
        page = query_params.get("page", 1)
        size = query_params.get("size", 10)

        # 校验前端传来的值是否合法
        validata_scheam = {
            "name": Validator(False, str),
            "account": Validator(False, str),
            "page": Validator(True, int, validata_page),
            "size": Validator(True, int, validata_size),
        }
        validata_data = {"name": name, "account": account, "page": int(page), "size": int(size)}
        params = RequestParamsValidator(validata_scheam).validate(validata_data)
        params = {key: value for key, value in params.items() if value}
        print(params)

        # 2. 把获取的参数传到 service 中, 来实现业务逻辑
        data = {"code": 200, "message": "查询成功", "data": UserInfoService.query(params)}

        return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
