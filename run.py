#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from util.test_http import TestLogin
from util.HTMLTestReportCN import HTMLTestRunner
from util import get_path


suit = unittest.TestSuite()
loader = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
suit.addTests(loader)

with open(get_path.test_report_path, 'wb') as file:
    runner = HTMLTestRunner(stream=file, verbosity=2, title='接口自动化测试报告', description='接口测试', tester="罗方")
    runner.run(suit)
