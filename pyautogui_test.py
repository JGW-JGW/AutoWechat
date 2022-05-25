# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021-11-15 19:23
# Author  : Seto.Kaiba
import random
import pyautogui
import pyperclip
from time import sleep
from sys import argv
from apscheduler.schedulers.background import BackgroundScheduler
import datetime as dt
import json
import win32com.client
import win32gui
import pythoncom
import win32con

"""
测试一下各种热键的操作灵不灵
"""


def wake_up():
    current_time = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')
    pyautogui.press('down')
    print('INFO: {} - 唤醒'.format(current_time))


def black_out():
    current_time = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')
    pyautogui.hotkey('win', 'x')
    sleep(0.5)
    pyautogui.press('u')
    sleep(0.5)
    pyautogui.press('s')
    print('INFO: {} - 黑屏'.format(current_time))


if __name__ == '__main__':
    # 模拟睡眠唤醒
    black_out()
    sleep(10)
    wake_up()
    sleep(5)

    # 置顶微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    sleep(0.5)
    pyautogui.doubleClick(16,46)
    sleep(1)

    # 定位窗口并置顶
    window = win32gui.FindWindow('WeChatMainWndForPC', '微信')
    win32gui.ShowWindow(window, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(window)


    # 获取上下左右的位置
    left, top, right, bottom = win32gui.GetWindowRect(window)

    # 点击搜索框
    pyautogui.click(left+130, top+37)





    # 置顶窗口
    # win32gui.ShowWindow(window, win32con.SW_SHOW)
    # pythoncom.CoInitialize()
    # shell = win32com.client.Dispatch("WScript.Shell")
    # shell.SendKeys('%')

    pass
