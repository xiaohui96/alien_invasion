#!/usr/bin/env python
# encoding: utf-8
"""
@author: xiaohui
@contact: xiaohui1295371450@163.com
@file: settings.py
@time: 2019-02-24 17:08
@desc:
"""


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230, 230, 230)
