# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021-11-13 14:28
# Author  : Seto.Kaiba
import random
import pyautogui
import pyperclip
from time import sleep
from sys import argv
from apscheduler.schedulers.background import BackgroundScheduler
import datetime as dt
import json
import win32gui
import win32con

"""
模拟人的键盘操作发送消息，目的是为了定时发送消息起到提醒的作用
"""

pyautogui.FAILSAFE = False


def get_friend():
    return '蒋家三人行'


def get_msg(time_str):
    msg_list = [
        '吃药',
        '该吃药了',
        '记得吃药',
        '请服药',
        '请用药'
    ]
    random_num = random.randint(0, len(msg_list) - 1)
    msg = msg_list[random_num]
    return '\n提醒时间：{}\n提醒任务：{}'.format(time_str, msg)


def show_time():
    print('当前时间：{}'.format(dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')))


def copy_and_paste(msg):
    pyperclip.copy(msg)
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')


def wake_up():
    current_time = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')
    pyautogui.press('down')
    print('INFO: {} - 唤醒'.format(current_time))


def black_out():
    current_time = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')
    pyautogui.hotkey('win', 'x')
    sleep(0.3)
    pyautogui.press('u')
    sleep(0.2)
    pyautogui.press('s')
    print('INFO: {} - 黑屏'.format(current_time))


def send_msg():
    current_time = dt.datetime.now()

    # 置顶微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    sleep(0.3)
    pyautogui.doubleClick(16, 46)
    sleep(0.5)

    # 获取窗口并置顶
    window = win32gui.FindWindow('WeChatMainWndForPC', '微信')
    if not window:
        raise WindowsError("捕捉窗口失败：微信")
    sleep(0.5)
    win32gui.ShowWindow(window, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(window)
    sleep(1)

    # 搜索好友
    left, top, right, bottom = win32gui.GetWindowRect(window)
    pyautogui.click(left + 130, top + 37)
    sleep(0.5)

    # 复制好友昵称到剪贴板
    copy_and_paste(get_friend())
    sleep(3)

    # 按回车进入好友聊天界面
    pyautogui.press('enter')
    sleep(0.5)

    # @某人
    pyautogui.press('@')
    sleep(3)
    pyautogui.press('enter')
    sleep(0.3)

    # 复制粘贴消息
    copy_and_paste(get_msg(current_time.strftime('%Y-%m-%d %H:%M')))
    sleep(1)

    # 按回车发送
    pyautogui.press('enter')
    sleep(1)

    # 最小化微信
    pyautogui.hotkey('ctrl', 'alt', 'w')

    print('INFO: {} - 发送消息'.format(current_time.strftime('%Y-%m-%d %H:%M:%S')))


background_scheduler = BackgroundScheduler(timezone='Asia/Shanghai')

send_msg_time_list = []
current_time = dt.datetime.now() + dt.timedelta(seconds=20)
for i in range(3):
    current_time = current_time + dt.timedelta(minutes=1)
    send_msg_time_list.append(current_time.strftime('%H:%M:%S'))

delta_time_before = 15  # seconds before send msg time
delta_time_after = 30  # seconds after send msg time

if len(argv) == 1:
    pass
elif len(argv) == 2 and argv[1].isdecimal():
    delta_time_before = int(argv[1])
    delta_time_after = int(argv[1])
elif len(argv) == 2 and not argv[1].isdecimal():
    send_msg_time_list = json.loads(argv[1])
elif len(argv) == 3 and argv[1].isdecimal() and not argv[2].isdecimal():
    delta_time_before = int(argv[1])
    delta_time_after = int(argv[1])
    send_msg_time_list = json.loads(argv[1])
elif len(argv) == 3 and argv[1].isdecimal() and argv[2].isdecimal():
    delta_time_before = int(argv[1])
    delta_time_after = int(argv[2])
elif len(argv) == 4 and argv[1].isdecimal() and argv[2].isdecimal() and not argv[3].isdecimal():
    delta_time_before = int(argv[1])
    delta_time_after = int(argv[2])
    send_msg_time_list = json.loads(argv[3])
else:
    raise ValueError("argv: {}".format(argv))
    exit(-1)

print('INFO: 唤醒前移：{:02d}秒'.format(delta_time_before))
print('INFO: 黑屏滞后：{:02d}秒'.format(delta_time_after))
print('INFO: 开始加载定时任务：')

count = 1
for item in send_msg_time_list:
    send_msg_time = dt.datetime.strptime(item, '%H:%M:%S')
    wake_up_time = send_msg_time - dt.timedelta(seconds=delta_time_before)
    black_out_time = send_msg_time + dt.timedelta(seconds=delta_time_after)
    print('INFO: {:02d} - 唤醒：{}，发送：{}，黑屏：{}'.format(
        count,
        wake_up_time.strftime('%H:%M:%S'),
        send_msg_time.strftime('%H:%M:%S'),
        black_out_time.strftime('%H:%M:%S')
    ))
    count += 1
    background_scheduler.add_job(
        wake_up,
        'cron',
        hour=wake_up_time.hour,
        minute=wake_up_time.minute,
        second=wake_up_time.second
    )
    background_scheduler.add_job(
        send_msg,
        'cron',
        hour=send_msg_time.hour,
        minute=send_msg_time.minute,
        second=send_msg_time.second
    )
    background_scheduler.add_job(
        black_out,
        'cron',
        hour=black_out_time.hour,
        minute=black_out_time.minute,
        second=black_out_time.second
    )

print('INFO: 定时任务加载完毕！')
print('INFO: 启动定时器')
background_scheduler.start()

while True:
    sleep(3600)

# pyinstaller --clean --noconfirm --collect-all backports.zoneinfo --collect-all pytz  --collect-all setuptools --collect-all six --collect-all tzdata --collect-all tzlocal -D wechat.py
# 把dist/site-packages里面的包考倒dist下，解决了找不到包的问题
