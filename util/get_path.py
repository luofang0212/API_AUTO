#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import time
import pathlib

# 获取路径
'''
1: os.path.split(path)——返回路径的目录和文件名，即将目录和文件名分开，而不是一个整体。此处只是把前后两部分分开而已。就是找最后一个'/'。
2: os.path.join(project_path,'test_result','html_report')  拼接路径
'''
# 获取文件当前路径
file_path = os.path.realpath(__file__)
# 获取该项目的顶级目录
project_path = os.path.split(os.path.split(file_path)[0])[0]

# 测试用例路径 excel文件
test_excel_path = os.path.join(project_path, 'test_data', 'testData.xlsx')

# 测试报告路径
test_report_path = os.path.join(project_path, 'test_result', 'html_report', 'test_report_1.html')

# 配置文件路径
read_config_path = os.path.join(project_path, 'config', 'case.config')

# 日志文件名生成
timestamp = time.strftime("%Y-%m-%d", time.localtime())
logfilename = 'api_auto' + '%s.log' % timestamp
# 日志文件路径
log_file_path = os.path.join(project_path, 'test_result', 'logs', logfilename)
