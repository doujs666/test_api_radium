# coding: utf-8
import unittest
from ddt import ddt, file_data
from api.demo_test_api import DemoTestApi


@ddt
class TestGetInfoUserApi(unittest.TestCase):
    @file_data("../script/test_demo.json")
    def test_demo(self, req, rep, result):
        print(req, rep, result)
        info_user = DemoTestApi()
        info_user.get(req)


    def test_custom_user(self):
        """
        查看用户单独购彩的购彩记录--全部数据
        :return:
        """
        info_user = DemoTestApi()
        info_user.get({"token": "123"})
        self.assertEquals(1,2)

