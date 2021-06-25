# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, data

from util.http_requests import HttpRequest
from util.do_excel import DoExcel
from util.get_data import GetData
from util import get_path
from util.do_logs import TestLog

log = TestLog().getlog()

# 执行case.config 中mode配置的用例
test_data = DoExcel().get_data(get_path.test_excel_path)

# 维护测试用例 2
@ddt
class TestLogin(unittest.TestCase):

    @data(*test_data)
    def test_api(self, item):
        user_token = getattr(GetData, 'USER_TOKEN')
        tel = getattr(GetData, 'PHONE')
        log.info("开始获取item里参数信息：user_token: {0}\n tel: {1}".format(user_token,tel))
        log.info("开始获取item：{0}".format(item))
        res = HttpRequest().http_request(item['method'], item['url'], eval(item['data']), eval(item['headers']))

        try:
            log.info("实际值：{0}，期望值:{1}".format(item['excepted'], res.json()['code']))
            self.assertEqual(item['excepted'], res.json()['code'])
            testResult = 'PASS'
        except Exception as e:
            testResult = 'Failed'
            log.error("错误信息：{0}".format(e))
            raise e
        finally:
            # 写入测试结果到excel
            DoExcel().write_back(get_path.test_excel_path,item['sheet_name'],item['case_id'] + 1, str(res.json()), testResult)
            log.info("sheet_name: {0}, case_id: {1}，测试结果：{2}".format(item['sheet_name'],item['case_id'],testResult))


