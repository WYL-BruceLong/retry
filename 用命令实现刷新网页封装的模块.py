# -*- coding: utf-8 -*-
# @Time    : 2018-10-31 21:47
# @Author  : BruceLong
# @Email   : 18656170559@163.com
# @File    : 用命令实现刷新网页封装的模块.py
# @Software: PyCharm

import requests
from retrying import retry

headers = {}


# 最大重试3次，3次全部报错，才会报错
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    # 超时的时候回报错并重试
    response = requests.get(url, headers=headers, timeout=3)
    # 状态码不是200，也会报错并重试
    assert response.status_code == 200
    return response


def parse_url(url):
    try:  # 进行异常捕获
        response = _parse_url(url)
    except Exception as e:
        print(e)
        # 报错返回None
        response = None
    return response
