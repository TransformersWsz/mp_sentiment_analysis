#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 21:56
# @Author  : Swift
# @File    : util.py
# @Brief   : 通用函数

import logging


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("crawler.log", mode="a")    # 日志输出到文件
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()    # 日志输出到控制台
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(message)s")    # 设置输出格式
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
