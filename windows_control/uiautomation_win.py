# coding = utf8

import os
import re
import subprocess
from time import sleep

import pyautogui

os.path.abspath(".")

import uiautomation
import pandas as pd
import time

# 实时获取时间
cur_time = time.strftime("%Y%m%d_%H%M%S")

"""
    绝大多数Windows软件的自动化控件操作等可以用uiautomation库来实现：
    1、Python-UIAutomation-for-Windows-master + uiautomation
    2、 automation.py（搜索控件）
    3、 pyautogui模拟键盘操作，快捷键等，对于一些uiautomation搜索不到的UI控件
"""


# 打开Potplayer，传入potplayer启动exe路径
def openPotplayer(potplayer_path="D:\PotPlayer\PotPlayerMini64.exe"):
    global potplayer
    potplayer = subprocess.Popen(potplayer_path)
    sleep(2)


# 进入Potplayer设备连接设置页面
def enterDeviceSettings():
    global potplayer_frame
    global settings_frame
    potplayer_frame = uiautomation.WindowControl(searchDepth=1, Name="PotPlayer")
    pyautogui.hotkey("alt", "d")
    settings_frame = uiautomation.WindowControl(searchDepth=2, Name="设备设置")


# 暂存格式列表
formatList = []


# 获取当前摄像头支持的格式
def getFormatList():
    settings_frame.ComboBoxControl(AutomationId="3008").Click()
    sleep(1)
    format_list = settings_frame.ListControl(searchDepth=5, Name="格式：")
    all_format = format_list.GetChildren()
    for format in all_format:
        formatList.append(format.Name)
    return formatList


# 遍历格式切换所有分辨率
def switchResolution(resolution="YUY2 960×540P 30(P 16:9)"):
    settings_frame.ComboBoxControl(AutomationId="3008").Click()
    sleep(1)
    find = False
    count = 0
    while not find:
        if count < 5:
            pyautogui.scroll(500)
        else:
            pyautogui.scroll(-500)
        count += 1
        resolution_checked = settings_frame.ListItemControl(searchDepth=6, Name=resolution)
        findResolution = str(re.findall("Rect:(.*)(\[)", str(resolution_checked))[0][0]).strip()
        if findResolution != "(0,0,0,0)":
            find = True
            resolution_checked.Click()
            break
    sleep(1)
    settings_frame.ButtonControl(searchDepth=3, Name="打开设备(O)").Click()
    sleep(1)


# 获取当前分辨率下的摄像头的帧率和位率并返回一个list
def getPlayerInformation():
    pyautogui.hotkey("ctrl", "f1")
    sleep(5)
    player_information = uiautomation.WindowControl(searchDepth=1, Name="播放信息")
    current_frameRate = player_information.TextControl(AutomationId="3201").GetWindowText()
    current_bitRate = player_information.TextControl(AutomationId="3386").GetWindowText()
    framerate = re.findall("->(.*)", current_frameRate)[0]
    bitrate = re.findall("\/(.*)\skbps", current_bitRate)[0]
    print("帧率：{} fps".format(framerate), end=" -- ")
    print("位率：{} kbps".format(bitrate))
    print("")
    return framerate, bitrate


# 关闭Potplayer
def closePotplayer():
    potplayer.kill()


# 标准数据和测试数据生成使用该方法生成，传入测试次数和测试结果列表进行每次测试数据的excel表格生成
def standard_test_DataGenerate(test_number="", result_list=[]):
    resolution_list = []
    frame_rate_list = []
    bit_rate_list = []
    for result in result_list:
        resolution_list.append(result[0])
        frame_rate_list.append(result[1])
        bit_rate_list.append(result[2])
    df = pd.DataFrame({"分辨率": resolution_list, "帧率": frame_rate_list, "位率": bit_rate_list})
    df.to_excel("./第{}次测试_resolutionTest.xlsx".format(test_number))


# 根据标准数据和测试数据对比返回过来的结果list进行生成最终的测试结果表格
def generateResult(checked_list=[]):
    resolution_list = []
    s_frame_rate_list = []
    s_bit_rate_list = []
    t_frame_rate_list = []
    t_bit_rate_list = []
    compare_result_list = []
    # [[分辨率、标准帧率、标准位率、测试帧率、测试位率、结果]、[]、[]……]
    for result in checked_list:
        resolution_list.append(result[0])
        s_frame_rate_list.append(result[1])
        s_bit_rate_list.append(result[2])
        t_frame_rate_list.append(result[3])
        t_bit_rate_list.append(result[4])
        compare_result_list.append(result[5])
    df = pd.DataFrame(
        {"分辨率": resolution_list, "标准帧率": s_frame_rate_list, "标准位率": s_bit_rate_list, "测试帧率": t_frame_rate_list,
         "测试位率": t_bit_rate_list, "测试结果": compare_result_list})
    df.to_excel("compare_result_{}.xlsx".format(str(cur_time)))


# 传入potplayer启动exe路径
def test_tandard_test_data(potplayerPath):
    result_list = []
    for i in range(2):
        try:
            openPotplayer(potplayer_path=potplayerPath)
            enterDeviceSettings()
            all_format = getFormatList()
            closePotplayer()
            for j in range(2, len(all_format)):
                resolution_now = all_format[j]
                print("第{}轮{}次测试 -- 当前测试分辨率为：{}".format(str(i + 1), str(j - 1), resolution_now))
                openPotplayer(potplayer_path=potplayerPath)
                enterDeviceSettings()
                switchResolution(resolution_now)
                list_cur = getPlayerInformation()
                closePotplayer()
                result_list.append([resolution_now, list_cur[0], list_cur[1]])
        except Exception as ex:
            print("Some error happened : {}".format(str(ex)))
            break
        finally:
            standard_test_DataGenerate(test_number=str(i + 1), result_list=result_list)
            result_list = []
            closePotplayer()


# 对比标准和测试数据并返回一个最终结果list
def compare2StandardDataTest():
    # 进行第二次测试，完善与第一次测试的数据比较并得出结果
    # 完善好后，学习PyQt5，将其转换成单独的工具：
    # 1、功能分开
    # 2、接口独立
    # 第二次测试和第一次测试数据进行读取后比较，再生成一个测试结果的Excel表格 -- ongoing
    standard_result = readExcel(path="./第1次测试_resolutionTest.xlsx")
    test_result = readExcel(path="./第2次测试_resolutionTest.xlsx")
    checked_list = []
    if len(standard_result) == len(test_result):
        print("Test result is the same count!")
        for i in range(0, len(standard_result)):
            item_list = []
            item_result = "FAIL"
            if standard_result[i][0] == test_result[i][0]:
                # print("Same row compare:当前check分辨率为：{}".format(standard_result[i][0]))
                s_frame = standard_result[i][1]
                s_bitRate = standard_result[i][2]
                t_frame = test_result[i][1]
                t_bitRate = test_result[i][2]
                if (abs(s_frame - t_frame) <= 3) & (abs(s_bitRate - t_bitRate) <= 1000):
                    item_result = "PASS"
                # 每行结果拼接：[分辨率、标准帧率、标准位率、测试帧率、测试位率、结果]
                item_list.append(standard_result[i][0])
                item_list.append(s_frame)
                item_list.append(s_bitRate)
                item_list.append(t_frame)
                item_list.append(t_bitRate)
                item_list.append(item_result)
            checked_list.append(item_list)
    else:
        print("Compare data length is different , please check your orignial data")
    if checked_list:
        print("Compare finished!")
        return checked_list
    else:
        return "Somethings error , please check your original data"


# 按结果格式，读取Excel表格
def readExcel(path="./第1次测试_resolutionTest.xlsx"):
    read = pd.read_excel(io=path, header=0, names=["分辨率", "帧率", "位率"], sheet_name="Sheet1")
    # print(read.values)  # 结果为[[],[],[]……]形式
    result = read.values
    return result
    # for i in read.values:
    # 分辨率
    # print(i[0])
    # 帧率
    # print(i[1])
    # 位率
    # print(i[2])


if __name__ == '__main__':
    potplayerPath = "D:\PotPlayer\PotPlayerMini64.exe"
    # test_tandard_test_data(potplayerPath)
    compareResult = compare2StandardDataTest()
    generateResult(compareResult)
