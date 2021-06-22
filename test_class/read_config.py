#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
from util import get_path

# 获取配置文件信息
class ReadConfig:

    def get_config(self,file_name, section, option):
        cf = configparser.ConfigParser()
        read = cf.read(file_name, encoding='utf-8')

        # 读取配置文件数据
        res = cf.get(section, option)

        return res


if __name__ == '__main__':
    res = ReadConfig().get_config(get_path.read_config_path,'MODE', 'mode')
    print(res)
