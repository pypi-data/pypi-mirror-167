# -*- coding:utf-8 -*-
# 文件:  jd_check.py
from .validate import verify


class JdCheck(object):
    """
    输入参数校验， 用于 web 请求参数校验
    """
    @staticmethod
    def verify(obj, **kwargs):  # 参数校验， 用法说明，请参考 verify 函数
        return verify(obj, **kwargs)
