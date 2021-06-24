#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from util import get_path

# 日志信息
'''
日志级别分别有：DEBUG，INFO，WARNING，ERROR，CRITICAL
logger 收集日志
handdler 输出日志渠道：指定文件夹，还是输出到控制台，默认是到控制台
'''


class MyLog:

    def my_log(self):
        # 收集日志
        my_logger = logging.getLogger('API_AUTO')
        my_logger.setLevel('DEBUG')  # 设置日志级别

        # 设置输出格式
        standard_format = logging.Formatter(
            "[%(asctime)s - %(name)s_%(filename)s:%(lineno)s %(levelname)s]日志信息: %(message)s")

        # 输出日志到指定渠道:输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(standard_format)

        # 输出日志到指定渠道:指定输出到文件
        fh = logging.FileHandler(get_path.log_file_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(standard_format)

        # 收集日志和输出渠道进行对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        # if level == 'DEBUG':
        #     my_logger.debug(msg)
        # elif level == 'INFO':
        #     my_logger.info(msg)
        # elif level == 'WARNING':
        #     my_logger.warning(msg)
        # elif level == 'ERROR':
        #     my_logger.error(msg)
        # elif level == 'CRITICAL':
        #     my_logger.critical(msg)

        # 关闭收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)


if __name__ == '__main__':
    # MyLog().debug('lisi')
    MyLog().my_log()
