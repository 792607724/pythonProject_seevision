# coding = utf8
import os
import re
import subprocess
from time import sleep

import pyautogui

pyautogui.FAILSAFE = True
from uiautomation import uiautomation

os.path.abspath(".")
"""
    @Project:pythonProject_seevision
    @File:windowsControl.py
    @Author:十二点前要睡觉
    @Date:2022/3/23 10:35
    @Description:通用HidTool、Potplayer控制文件，可复用
"""


def openPotplayer(potplayer_path="D:\PotPlayer\PotPlayerMini64.exe"):
    """
    打开Potplayer
    :param potplayer_path:你本机的Potplayer启动软件的路径
    :return:None
    """
    global potplayer
    potplayer = subprocess.Popen(potplayer_path)
    sleep(2)
    if uiautomation.TextControl(searchDepth=3, Name="检查更新：").Exists():
        pyautogui.press("esc")


def enterDeviceSettings():
    """
    进入Potplayer设备设置页
    :return:None
    """
    global potplayer_frame
    global settings_frame
    potplayer_frame = uiautomation.WindowControl(searchDepth=1, Name="PotPlayer")
    pyautogui.hotkey("alt", "d")
    settings_frame = uiautomation.WindowControl(searchDepth=2, Name="设备设置")


def switchResolution(resolution="YUY2 960×540P 30(P 16:9)"):
    """
    Potplayer切换指定分辨率（滚动查找）
    :param resolution:需要切换的分辨率
    :return:None
    """
    settings_frame.ComboBoxControl(AutomationId="3008").Click()
    settings_frame.SetFocus()
    sleep(1)
    find = False
    count = 0
    while not find:
        if resolution:
            resolution_checked = settings_frame.ListItemControl(searchDepth=6, Name=resolution)
            findResolution = str(re.findall("Rect:(.*)(\[)", str(resolution_checked))[0][0]).strip()
            if findResolution != "(0,0,0,0)":
                find = True
                resolution_checked.Click()
                break
        else:
            print("Resolution error")
        if count < 10:
            pyautogui.scroll(500)
            sleep(0.5)
        else:
            pyautogui.scroll(-500)
            sleep(0.5)
        count += 1
        sleep(0.5)
    sleep(1)
    settings_frame.ButtonControl(searchDepth=3, Name="打开设备(O)").Click()
    sleep(5)


def openHidTool(hidtool_path="D:\HIDTools_2.5\HIDTool_2_5.exe"):
    """
    打开HidTool2.5工具
    :param hidtool_path:你本机的HidTool启动软件的路径
    :return:None
    """
    global hidtool
    hidtool = subprocess.Popen(hidtool_path)
    sleep(2)


def closeHidTool():
    """
    关闭HidTool2.5工具
    :return:None
    """
    if hidtool:
        hidtool.kill()
    sleep(1)


# 关闭Potplayer
def closePotplayer():
    """
    关闭Potplayer
    :return:None
    """
    if potplayer:
        potplayer.kill()
    sleep(1)


# 放大
def hidZoomIn(step):
    """
    HidTool放大操作
    :param step:放大的步长
    :return:None
    """
    step_edit = uiautomation.EditControl(AutomationId="eptz_size_textbox_length")
    step_edit.GetValuePattern().SetValue("")
    step_edit.SendKeys(str(step))
    uiautomation.ButtonControl(AutomationId="button2").Click()
    sleep(1)


# 缩小
def hidZoomOut(step):
    """
    HidTool缩小操作
    :param step:缩小的步长
    :return:None
    """
    step_edit = uiautomation.EditControl(AutomationId="eptz_size_textbox_length")
    step_edit.GetValuePattern().SetValue("")
    step_edit.SendKeys(str(step))
    uiautomation.ButtonControl(AutomationId="button3").Click()
    sleep(1)


# 复位
def hidReset():
    """
    HidTool缩放复位操作
    :return:None
    """
    uiautomation.ButtonControl(AutomationId="button4").Click()
    sleep(1)


def rightNarrow(step):
    """
    HidTool右移操作
    :param step:右移动的步长
    :return:None
    """
    print("开始右移动【{}】step".format(step))
    step_edit = uiautomation.EditControl(AutomationId="eptz_move_textbox_length")
    step_edit.GetValuePattern().SetValue("")
    step_edit.SendKeys(str(step))
    uiautomation.ButtonControl(AutomationId="right_narrow").Click()
    sleep(1)


# 获取当前摄像头支持的格式
def getFormatList():
    """
    通过Potplayer获取当前摄像头支持的分辨率格式
    :return:返回所支持的分辨率格式列表
    """
    settings_frame.ComboBoxControl(AutomationId="3008").Click()
    sleep(1)
    format_list = settings_frame.ListControl(searchDepth=5, Name="格式：")
    all_format = format_list.GetChildren()
    formatList = []
    for format in all_format:
        # 筛选掉重复的分辨率格式
        if (str(format) != "开始播放时选择格式") | (str(format) != "默认格式(推荐)"):
            if "(P" in str(format):
                formatList.append(format.Name)
    return formatList


if __name__ == '__main__':
    """
        用于调试
    """
    """
    ['YUY2 640×360P 30(P 16:9)', 'YUY2 160×90P 30(P 16:9)', 'YUY2 160×120P 30(P 4:3)', 'YUY2 176×144P 30(P 11:9)',
     'YUY2 320×180P 30(P 16:9)', 'YUY2 320×240P 30(P 4:3)', 'YUY2 352×288P 30(P 11:9)', 'YUY2 480×270P 30(P 16:9)',
     'YUY2 640×480P 30(P 4:3)', 'YUY2 800×600P 30(P 4:3)', 'YUY2 960×540P 30(P 16:9)', 'MJPG 1920×1080P 30(P 16:9)',
     'MJPG 160×90P 30(P 16:9)', 'MJPG 160×120P 30(P 4:3)', 'MJPG 176×144P 30(P 11:9)', 'MJPG 320×180P 30(P 16:9)',
     'MJPG 320×240P 30(P 4:3)', 'MJPG 352×288P 30(P 11:9)', 'MJPG 480×270P 30(P 16:9)', 'MJPG 640×360P 30(P 16:9)',
     'MJPG 640×480P 30(P 4:3)', 'MJPG 800×600P 30(P 4:3)', 'MJPG 960×540P 30(P 16:9)', 'MJPG 1024×576P 30(P 16:9)',
     'MJPG 1280×720P 30(P 16:9)', 'MJPG 2560×1440P 30(P 16:9)', 'MJPG 3840×2160P 30(P 16:9)',
     'H264 1920×1080P 30(P 16:9)', 'H264 1280×720P 30(P 16:9)', 'H264 1024×576P 30(P 16:9)', 'H264 960×540P 30(P 16:9)',
     'H264 800×600P 30(P 4:3)', 'H264 640×480P 30(P 4:3)', 'H264 640×360P 30(P 16:9)', 'H264 480×270P 30(P 16:9)',
     'H264 352×288P 30(P 11:9)', 'H264 320×240P 30(P 4:3)', 'H264 320×180P 30(P 16:9)', 'H264 2560×1440P 30(P 16:9)',
     'H264 3840×2160P 30(P 16:9)']
     """
    potplayer_path = r"D:\PotPlayer\PotPlayerMini64.exe"
    openPotplayer(potplayer_path)
    enterDeviceSettings()
    resolution = "YUY2 960×540P 30(P 16:9)"
    switchResolution(resolution)
    hidtool_path = r"D:\HIDTools_2.5\HIDTool_2_5.exe"
    openHidTool(hidtool_path)
    hidZoomIn(5)
    # hidZoomOut(1)
    # rightNarrow(1)
    hidReset()
