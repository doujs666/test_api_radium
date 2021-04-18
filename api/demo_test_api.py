# -*- coding:utf-8 -*-
from base.base_api import BaseApi


class DemoTestApi(BaseApi):
    """
    示例
    """
    url = "/api/i/wallet/usercertify"

    def build_custom_param(self, data):
        return {'token': data['token']}
