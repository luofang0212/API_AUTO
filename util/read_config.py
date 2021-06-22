#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
from util import get_path

# 获取配置文件信息
class ReadConfig:

    def get_config(self,file_name, section, option):
        cf = configparser.ConfigParser()
        read = cf.read(file_name, encoding='utf-8')
        # section：指块 --> [MODE], option 对应的key --> mode, value
        # 第一种方式：读取配置文件数据
        res = cf.get(section, option)

        return res
        # print(res)

        # # 第二种方式：读取配置文件数据
        # res_2 = cf[section][option]
        # # print(res_2)

if __name__ == '__main__':
    res = ReadConfig().get_config(get_path.read_config_path,'MODE', 'mode')
    print(res)
