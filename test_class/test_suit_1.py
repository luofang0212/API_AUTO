# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from util.test_http import TestLogin
from util.HTMLTestReportCN import HTMLTestRunner
from util import get_path


# 加载测试用例、生成测试报告
class TestSuitReport:

    def test_report(self):
        # 创建测试套件
        suit = unittest.TestSuite()
        loader = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

        # 将需要测试的用例加载到测试套件中
        suit.addTests(loader)

        with open(get_path.test_report_path, 'wb') as file:
            runner = HTMLTestRunner(stream=file, verbosity=2, title='接口自动化测试报告', description='接口测试', tester="罗方")
            # 运行测试用例
            runner.run(suit)


if __name__ == '__main__':
    TestSuitReport().test_report()
