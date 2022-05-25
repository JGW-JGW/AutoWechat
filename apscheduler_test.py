# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021-11-13 15:14
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import datetime as dt


"""
测试任务调度框架
"""


def show_time():
    print('show_time: {}'.format(dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')))


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(show_time, 'interval', seconds=2, timezone='Asia/Shanghai', jitter=600)
    scheduler.start()
    pass