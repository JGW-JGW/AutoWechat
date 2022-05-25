# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021-11-16 19:57
# Author  : Seto.Kaiba
import multiprocessing as jc
import time
import tkinter as tk
import win32api as wa
import win32con as wn
import win32gui as wg


def init_window():
    global cs, wd
    wd = tk.Tk()
    cs = tk.Canvas(wd,
                   width=800,
                   height=500,
                   bg='white')
    wd.minsize(800, 500)  # 最小尺寸
    wd.maxsize(800, 500)
    wd.title('DDTHelper')
    pic = tk.PhotoImage(file="pic.png")
    cs.create_image(400, 250, image=pic)
    cs.pack()
    bt = tk.Button(wd,
                   text='初始化',
                   bg=('white'),
                   font=('微软雅黑', 20),
                   width=155,
                   height=48,
                   command=BT_onCreat)
    bt.pack()
    cs.create_window(530, 70,
                     width=155,
                     height=48,
                     window=bt)
    wd.mainloop()


def init_control(Znum, name):
    global v1, v2, v3, tx1, t2, tx2, t3, tx3, txn1, txn2, txn3
    if Znum == 1:
        v1 = tk.IntVar()
        tx1 = tk.StringVar()
        # txn1=tk.StringVar()
    elif Znum == 2:
        v2 = tk.IntVar()
        tx2 = tk.StringVar()
        # txn2=tk.StringVar()
    elif Znum == 3:
        v3 = tk.IntVar()
        tx3 = tk.StringVar()
        # txn3=tk.StringVar()
    exec('tx{}.set("未运行")'.format(Znum))
    exec('lb{} = tk.Label(wd,text="{}",bg=("#ffffff"),font=("微软雅黑",20))'.format(Znum, name))
    # exec('lbn{} = tk.Label(wd,textvariable=txn{},bg=("#ffffff"),font=("微软雅黑",10))'.format(Znum,Znum))
    exec(
        'cb{} = tk.Checkbutton(wd,textvariable=tx{},bg=("#ffffff"),font=("微软雅黑",10),variable = v{}, height=5,width = 0,command=BT_onRun{})'.format(
            Znum, Znum, Znum, Znum))
    exec('cb{}.pack()'.format(Znum))
    exec('lb{}.pack()'.format(Znum))
    # exec('lbn{}.pack()'.format(Znum))
    Ytmp = Znum * 100
    Ytmp = Ytmp + 70
    exec('cs.create_window(630,{},width=0,height=0,window=lb{})'.format(Ytmp, Znum))
    Ytmp = Ytmp + 40
    # exec('cs.create_window(630,{},width=35,height=25,window=lbn{})'.format(Ytmp,Znum))
    exec('cs.create_window(710,{},width=70,height=25,window=cb{})'.format(Ytmp, Znum))


def BT_onCreat():
    global Znum, D1, D2, D3, conT
    Znum = 0
    wg.EnumWindows(get_all_hwnd, 0)
    conT = jc.Manager().Array("i", [3, 0, 0, 0])
    for h, t in hwnd_title.items():
        if "4399" in t:
            hwnd = t.split("|")[3]
            name = t.split("|")[2]
            print("账号：" + name + "句柄：" + hwnd)
            Znum = Znum + 1
            hwnd = int(hwnd)
            init_control(Znum, name)
            if Znum == 1:
                D1 = jc.Manager().Array("i", [1, hwnd])
            elif Znum == 2:
                D2 = jc.Manager().Array("i", [2, hwnd])
            elif Znum == 3:
                D3 = jc.Manager().Array("i", [3, hwnd])


def get_all_hwnd(hwnd, mouse):
    if wg.IsWindow(hwnd) and wg.IsWindowEnabled(hwnd) and wg.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: wg.GetWindowText(hwnd)})


def all_run(Znum):
    while Znum > 0:
        exec('t{}.start()'.format(Znum))
        Znum = Znum - 1


# 操作类--------------------------------------------------------------------------------------------------------------
def climb(hwnd, jl, fx):
    if fx == 1:  # 右边
        # 适应方向及防止无效
        wa.SendMessage(hwnd, wn.WM_KEYDOWN, 68, None)
        wa.SendMessage(hwnd, wn.WM_KEYUP, 68, None)
        # 1.3=1屏距
        wa.SendMessage(hwnd, wn.WM_KEYDOWN, 68, None)
        time.sleep(jl * 1.3)
        wa.SendMessage(hwnd, wn.WM_KEYUP, 68, None)
    else:
        # 适应方向及防止无效
        wa.SendMessage(hwnd, wn.WM_KEYDOWN, 65, None)
        wa.SendMessage(hwnd, wn.WM_KEYUP, 65, None)
        # 1.3=1屏距
        wa.SendMessage(hwnd, wn.WM_KEYDOWN, 65, None)
        time.sleep(jl * 1.3)
        wa.SendMessage(hwnd, wn.WM_KEYUP, 65, None)


def doAngle(hwnd, jd):
    for i in range(jd):
        time.sleep(0.05)
        wa.SendMessage(hwnd, wn.WM_KEYDOWN, 87, None)
        wa.SendMessage(hwnd, wn.WM_KEYUP, 87, None)


def doClick(hwnd, cx, cy):
    long_position = wa.MAKELONG(cx, cy)
    wa.SendMessage(hwnd, wn.WM_LBUTTONDOWN, wn.MK_LBUTTON, long_position)
    wa.SendMessage(hwnd, wn.WM_LBUTTONUP, wn.MK_LBUTTON, long_position)


def doFire(hwnd, ld):
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 66, None)  # 先摁大
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 69, None)  # 先摁技能
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 97, None)
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 98, None)
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 97, None)  # 11大招
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 100, None)
    wa.SendMessage(hwnd, wn.WM_KEYDOWN, 32, None)
    time.sleep(ld * 0.04)
    wa.SendMessage(hwnd, wn.WM_KEYUP, 32, None)


# 游戏流程处理类---------------------------------------------------------------------------------------------------------
def Chose_FB(hwnd, hdc):
    doClick(hwnd, 600, 200)  # 打开菜单
    time.sleep(1)
    doClick(hwnd, 626, 188)  # 单人副本
    time.sleep(1)
    while True:
        doClick(hwnd, 5, 5)
        if str(wg.GetPixel(hdc, 244, 237)) == str(2041582):
            doClick(hwnd, 289, 243)  # 魔石
            FBn = 1
            break
        elif str(wg.GetPixel(hdc, 337, 278)) == str(13298869):
            doClick(hwnd, 292, 299)  # 技能丹
            FBn = 2
            break
    time.sleep(1)
    doClick(hwnd, 726, 501)  # 难度
    time.sleep(1)
    doClick(hwnd, 504, 563)  # 确定
    time.sleep(1)
    doClick(hwnd, 951, 491)
    return (FBn)


def FB_MS(hwnd, hdc):
    time.sleep(24)
    while str(wg.GetPixel(hdc, 497, 169)) != str(5418993):  # 回合检测
        doClick(hwnd, 5, 5)
        time.sleep(0.5)
    while True:
        doClick(hwnd, 5, 5)
        colx = wg.GetPixel(hdc, 917, 486)
        if str(colx) == str(36645):
            print("位置1")
            JD = 18
            break
        else:
            print("位置2")
            climb(hwnd, 0.5, 0)
            JD = 25
            break
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 69, None)  # 波谷专用
    wa.SendMessage(hwnd, wn.WM_KEYFIRST, 80, None)  # 第一次pass
    time.sleep(5)
    for i in range(2):
        while str(wg.GetPixel(hdc, 497, 169)) != str(5418993):  # 回合检测
            doClick(hwnd, 5, 5)
            time.sleep(0.5)
        wa.SendMessage(hwnd, wn.WM_KEYDOWN, 65, None)
        wa.SendMessage(hwnd, wn.WM_KEYUP, 65, None)
        doFire(hwnd, 20)
    time.sleep(6)
    doAngle(hwnd, JD)
    time.sleep(10)
    while True:
        # 回合循环
        cs = 0
        while str(wg.GetPixel(hdc, 497, 169)) != str(5418993):  # 回合检测
            if cs >= 20:  # 超时退出
                break
            else:
                doClick(hwnd, 5, 5)
                time.sleep(1)
                cs = cs + 1
        # 退出
        if cs == 20:
            print("退出副本")
            break
        else:
            doFire(hwnd, 20)


def FB_JD(hwnd, hdc):
    while True:
        cs = 0
        cg = 0
        while str(wg.GetPixel(hdc, 497, 169)) != str(5418993):  # 回合检测
            if cs >= 20:  # 超时退出
                cg = 1
                cs = 0
                break
            else:
                doClick(hwnd, 5, 5)
                time.sleep(1)
                cs = cs + 1
        if cg == 1:
            break
        else:
            doFire(hwnd, 60)


# 程序流程模块类----------------------------------------------------------------------------------------------------------
def RunMain(hwnd):
    RM = 0
    hdc = wg.GetWindowDC(hwnd)
    while True:
        while str(wg.GetPixel(hdc, 919, 280)) != str(10248996):  # 房间检测
            print("房间")
            doClick(hwnd, 5, 5)
            time.sleep(1)
        if Chose_FB(hwnd, hdc) == 1:
            FB_MS(hwnd, hdc)
        else:
            FB_JD(hwnd, hdc)
        RM = RM + 1


def Con(Data, conT):
    # 设置守护线程
    Znum = Data[0]
    print(str(Data[0]))
    hwnd = Data[1]
    time.sleep(1)
    exec('t{} = xc.Thread(target=RunMain,args=(hwnd,))'.format(Znum))
    exec('t{}.setDaemon(True)'.format(Znum))
    exec('t{}.start()'.format(Znum))
    while True:
        if conT[Znum] == 0:
            time.sleep(1)
        else:
            break
    print('进程' + str(Znum) + '：已退出')


def onRunMan(Znum):
    if onRunMan2(Znum) == 1:
        conT[Znum] = 0
        exec('tx{}.set("运行中")'.format(Znum))
        exec('p{} = jc.Process(target=Con,args=(D{},conT))'.format(Znum, Znum))
        exec('p{}.daemon=True'.format(Znum))
        exec('p{}.start()'.format(Znum))
    else:
        conT[Znum] = 1
        # exec('del p{}'.format(Znum))
        exec('tx{}.set("未运行")'.format(Znum))


def onRunMan2(Znum):
    if Znum == 1:
        return v1.get()
    elif Znum == 2:
        return v2.get()
    elif Znum == 3:
        return v3.get()


def onRunMan3(Znum):
    if Znum == 1:
        if p1.is_alive:
            return (1)
        else:
            return (0)
    elif Znum == 2:
        if p2.is_alive:
            return (1)
        else:
            return (0)
    elif Znum == 3:
        if p3.is_alive:
            return (1)
        else:
            return (0)


def BT_onRun1():
    onRunMan(1)


def BT_onRun2():
    onRunMan(2)


def BT_onRun3():
    onRunMan(3)


if __name__ == '__main__':
    hwnd_title = dict()
    init_window()