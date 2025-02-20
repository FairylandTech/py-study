# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-20 20:38:31 UTC+08:00
"""
from django.http.response import JsonResponse


class OverrideJsonResponse(JsonResponse):

    def __init__(self, *args, **kwargs):
        json_dumps_params = {"ensure_ascii": False}
        super().__init__(json_dumps_params=json_dumps_params, *args, **kwargs)
