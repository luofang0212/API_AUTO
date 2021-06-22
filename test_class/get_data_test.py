#!/usr/bin/env python
# -*- coding: utf-8 -*-

#反射

class GetDate:
    COOKIE = None


if __name__ == '__main__':
    print(getattr(GetDate,'COOKIE'))  #getattr 获取属性值
    setattr(GetDate,'COOKIE','12345') #setattr 设置属性值
    print(getattr(GetDate, 'COOKIE'))  # getattr 获取属性值
    print(delattr(GetDate, 'COOKIE'))  # delattr 删除属性
    print(hasattr(GetDate, 'COOKIE')) # hasattr 判断是否有这个属性