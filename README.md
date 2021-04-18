API测试框架概要
===

涉及到的包
___

1、基于python V3.6.4<br>
2、基于Requests V2.18.4<br>
3、基于HTMLTestrunner V0.8.0<br>
4、基于ddt v1.4.2<br>

1.目录介绍
___
config-properties放置配置文件<br>
api放置封装的api接口<br>
base放置各种基础封装<br>
log放置log和截图文件<br>
result放置生成的测试报告和json数据<br>
script放置自定义脚本文件<br>
test_case放置测试用例<br>
parameter放置ddt入参文件<br>

2.baseApi
___
1、url拼接处理----已完成<br>
2、参数拼接处理----已完成<br>
3、POST/GET请求方式封装，针对不同接口类型封装不同HEADERS----已完成<br>

3.api
___
api封装介绍（接口封装时将该方法重写）----已完成<br>
```python
def build_custom_param(self, data):
    return {'test': data['test']}
```
4.parameter
___
入参有3个，分别是req,rep,result<br>
```python
{
  "接口调用成功": {
    "req": {
      "token": "AA"
    },
    "rep": {
      "status": "success",
      "data": {
        "message": "登录成功",
      }
    },
    "result": 2
  },
  "token错误": {
    "req": {
      "token": "obP"
    },
    "rep": {
      "status": "fail",
      "data": {
        "message": "登录失败"
      }
    },
    "result": 1
  }
}
```
5.test_case
___
有2种调用方法<br>
第一种入参是读取scriot目录的json文件-----已完成<br>
```python
@ddt
class TestGetInfoUserApi(unittest.TestCase):
    @file_data("../script/test_demo.json")
    def test_demo(self, req, rep, result):
        print(req, rep, result)
        info_user = DemoTestApi()
        info_user.get(req)
        
```
第二种入参是自己传入-----已完成<br>
```python
    def test_custom_user(self):
        """
        测试失败
        :return:
        """
        info_user = DemoTestApi()
        info_user.get({"token": "123"})
        self.assertEquals(1,2)
```

6.HTMLTestrunner
___
1、定制python3-------已完成<br>
2、定制测试报告模板---—-已完成<br>

7.BaseEmail
___
1、自动获取最新测试报告-----已完成<br>
2、发送邮件、附件、图片-----已完成<br>

8.BaseThread
___
1、实现Case内部可使用多线程-----未完成<br>
2、可获取所有线程函数的返回值-- --未完成<br>

9.BaseLog
___
1、日志双输出，需可控，日志可同时打印到控制台和输出到日志文件中----未完成<br>

10.BaseRunner
___
1、统计Case数量----------已完成<br>
2、记录Case运行时间----------已完成<br>
3、输出测试报告----------已完成<br>
4、失败后重试（只重新失败case）---未完成<br>

11.BaseMysql
___
1、数据库连接----------已完成<br>
2、select返回多行或单行----------已完成<br>

12.BaseRedis
___
1、Redis链接----------已完成<br>
2、Redis常用命令封装----------已完成<br>

13.config-properties
___
1、读取settings.py文件----------已完成<br>
2、读取xml文件----------未完成<br>
3、动态获取环境包括数据库地址，url,redis----未完成<br>


14.性能测试
___
1、并发——————未完成<br>



