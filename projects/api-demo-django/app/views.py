# Create your views here.

import json

from django.http.request import HttpRequest
from django.http.response import HttpResponseBase, JsonResponse
from django.views import View

from fairylandfuture.structures.builder.db import StructureMySQLExecute
from utils.db import dbtools
from fairylandfuture.modules.validator.validators import Validator, RequestParamsValidator

from urllib.parse import parse_qs
from app.services import UserInfoService
from utils.journal import journal
from utils.api.response import OverrideJsonResponse
from utils.structutes.response import StructureResponse


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
    service = UserInfoService

    def get(self, request: HttpRequest) -> HttpResponseBase:
        journal.info(f"用户视图::查询::{self.__class__.__name__}")

        query_params = request.GET
        response: StructureResponse = StructureResponse()

        try:
            # 1. 获取前端传来的查询参数
            pk = query_params.get("id", 0)
            name = query_params.get("name")
            account = query_params.get("account")
            page = query_params.get("page", 1)
            size = query_params.get("size", 10)

            try:
                # 校验前端传来的值是否合法
                validata_scheam = {
                    "id": Validator(False, int),
                    "name": Validator(False, str),
                    "account": Validator(False, str),
                    "page": Validator(True, int, validata_page),
                    "size": Validator(True, int, validata_size),
                }
                validata_data = {"id": int(pk), "name": name, "account": account, "page": int(page), "size": int(size)}
                params = RequestParamsValidator(validata_scheam).validate(validata_data)
                params = {key: value for key, value in params.items() if value}
            except Exception as err:
                journal.error(str(err))
                response.message = "参数校验错误"
                raise RuntimeError("参数校验错误")

            # 2. 把获取的参数传到 service 中, 来实现业务逻辑
            data = UserInfoService.query(params)

            response.code = 200
            response.message = "查询成功"
            response.data = data

            journal.success(f"用户视图::查询用户成功::{self.__class__.__name__}")
        except Exception as err:
            journal.error(str(err))
            response.code = 500
            response.message = "服务器内部错误" if not response.message else response.message
            journal.error(f"用户视图::查询用户失败::{self.__class__.__name__}")
        finally:
            return OverrideJsonResponse(response.asdict)

    def post(self, request: HttpRequest) -> HttpResponseBase:
        response: StructureResponse = StructureResponse()
        # params = request.POST  # body 中 form-data 的数据
        # params = request.FILES.get("file")  # body 中 使用 form-data 传来的文件类型, 获取到的是文件流

        # raw -- JSON, json.loads(request.body)  -> 转为 python 中的字典来使用, request.body 是一个字节类型的字符串IO流
        # x-www-form-urlencodeed, urllib.parse, parse_sq, 用来解析 urlencoded 格式的数据
        # raw_parse = {k: v[0] for k, v in parse_qs(raw).items()}

        query_dict = json.loads(request.body)
        try:
            # 校验数据合法性
            flag = self.service.add(query_dict)
            if flag:
                response.code = 201
                response.message = "新增成功"
            else:
                raise RuntimeError("未知错误")
        except Exception as err:
            journal.error(str(err))
            response.code = 500
            response.message = "新增失败"
        finally:
            return OverrideJsonResponse(response.asdict)

    def delete(self, request: HttpRequest) -> HttpResponseBase:
        response = StructureResponse()

        query_dict = request.GET
        try:
            _id = query_dict.get("id")
            if not _id:
                raise Exception

            if self.service.delete(_id):
                response.code = 204
                response.message = "删除成功"
            else:
                response.code = 500
        except Exception as err:
            journal.error(str(err))
            response.code = 500

        finally:
            return OverrideJsonResponse(response.asdict)
