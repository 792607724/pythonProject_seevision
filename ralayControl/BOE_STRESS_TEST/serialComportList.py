# coding = utf8
import os

os.path.abspath(".")
"""
    @Project:PycharmProjects
    @File:serialComportList.py
    @Author:十二点前要睡觉
    @Date:2021/12/14 10:36
"""
"""
    情景      	    RTU格式（16进制发送）
    查询十六路状态	    [0xFE, 0x01, 0x00, 0x00, 0x00, 0x10, 0x29, 0xC9]
    查询指令返回信息	[0xFE, 0x01, 0x01, 0x00, 0x61, 0x9C]
    控制第一路开	    [0xFE, 0x05, 0x00, 0x00, 0xFF, 0x00, 0x98, 0x35]
    控制返回信息	    [0xFE, 0x05, 0x00, 0x00, 0xFF, 0x00, 0x98, 0x35]
    控制第一路关	    [0xFE, 0x05, 0x00, 0x00, 0x00, 0x00, 0xD9, 0xC5]
    控制返回信息	    [0xFE, 0x05, 0x00, 0x00, 0x00, 0x00, 0xD9, 0xC5]
    控制第二路开	    [0xFE, 0x05, 0x00, 0x01, 0xFF, 0x00, 0xC9, 0xF5]
    控制第二路关	    [0xFE, 0x05, 0x00, 0x01, 0x00, 0x00, 0x88, 0x05]
    控制第三路开	    [0xFE, 0x05, 0x00, 0x02, 0xFF, 0x00, 0x39, 0xF5]
    控制第三路关	    [0xFE, 0x05, 0x00, 0x02, 0x00, 0x00, 0x78, 0x05]
    控制第四路开	    [0xFE, 0x05, 0x00, 0x03, 0xFF, 0x00, 0x68, 0x35]
    控制第四路关	    [0xFE, 0x05, 0x00, 0x03, 0x00, 0x00, 0x29, 0xC5]
    控制第五路开	    [0xFE, 0x05, 0x00, 0x04, 0xFF, 0x00, 0xD9, 0xF4]
    控制第五路关	    [0xFE, 0x05, 0x00, 0x04, 0x00, 0x00, 0x98, 0x04]
    控制第六路开	    [0xFE, 0x05, 0x00, 0x05, 0xFF, 0x00, 0x88, 0x34]
    控制第六路关	    [0xFE, 0x05, 0x00, 0x05, 0x00, 0x00, 0xC9, 0xC4]
    控制第七路开	    [0xFE, 0x05, 0x00, 0x06, 0xFF, 0x00, 0x78, 0x34]
    控制第七路关	    [0xFE, 0x05, 0x00, 0x06, 0x00, 0x00, 0x39, 0xC4]
    控制第八路开	    [0xFE, 0x05, 0x00, 0x07, 0xFF, 0x00, 0x29, 0xF4]
    控制第八路关	    [0xFE, 0x05, 0x00, 0x07, 0x00, 0x00, 0x68, 0x04]
    控制第九路开	    [0xFE, 0x05, 0x00, 0x08, 0xFF, 0x00, 0x19, 0xF7]
    控制第九路关	    [0xFE, 0x05, 0x00, 0x08, 0x00, 0x00, 0x58, 0x07]
    控制第十路开	    [0xFE, 0x05, 0x00, 0x09, 0xFF, 0x00, 0x48, 0x37]
    控制第十路关	    [0xFE, 0x05, 0x00, 0x09, 0x00, 0x00, 0x09, 0xC7]
    控制第十一路开	    [0xFE, 0x05, 0x00, 0x0A, 0xFF, 0x00, 0xB8, 0x37]
    控制第十一路关	    [0xFE, 0x05, 0x00, 0x0A, 0x00, 0x00, 0xF9, 0xC7]
    控制第十二路开	    [0xFE, 0x05, 0x00, 0x0B, 0xFF, 0x00, 0xE9, 0xF7]
    控制第十二路关	    [0xFE, 0x05, 0x00, 0x0B, 0x00, 0x00, 0xA8, 0x07]
    控制第十三路开	    [0xFE, 0x05, 0x00, 0x0C, 0xFF, 0x00, 0x58, 0x36]
    控制第十三路关	    [0xFE, 0x05, 0x00, 0x0C, 0x00, 0x00, 0x19, 0xC6]
    控制第十四路开	    [0xFE, 0x05, 0x00, 0x0D, 0xFF, 0x00, 0x09, 0xF6]
    控制第十四路关	    [0xFE, 0x05, 0x00, 0x0D, 0x00, 0x00, 0x48, 0x06]
    控制第十五路开	    [0xFE, 0x05, 0x00, 0x0E, 0xFF, 0x00, 0xF9, 0xF6]
    控制第十五路关	    [0xFE, 0x05, 0x00, 0x0E, 0x00, 0x00, 0xB8, 0x06]
    控制第十六路开	    [0xFE, 0x05, 0x00, 0x0F, 0xFF, 0x00, 0xA8, 0x36]
    控制第十六路关	    [0xFE, 0x05, 0x00, 0x0F, 0x00, 0x00, 0xE9, 0xC6]
"""
"""
    Control AlL:
    1、查询16路状态
    2、查询指令返回信息
"""
RELAY_CONTROL_CHECK_ALL_COMPORT_STATUS = [0xFE, 0x01, 0x00, 0x00, 0x00, 0x10, 0x29, 0xC9]
RELAY_CONTROL_CHECK_ALL_COMPORT_STATUS_RETURN = [0xFE, 0x01, 0x01, 0x00, 0x61, 0x9C]

RELAY_CONTROL_COMPORT_OPEN_ALL = [0xFE, 0x0F, 0x00, 0x00, 0x00, 0x10, 0x02, 0xFF, 0xFF, 0xA6, 0x64]
RELAY_CONTROL_COMPORT_CLOSE_ALL = [0xFE, 0x0F, 0x00, 0x00, 0x00, 0x10, 0x02, 0x00, 0x00, 0xA7, 0xD4]
"""
    Control Single
    1、控制第一路开
    2、控制返回信息
    3、控制第一路关
"""
RELAY_CONTROL_COMPORT_1_OPEN = [0xFE, 0x05, 0x00, 0x00, 0xFF, 0x00, 0x98, 0x35]
RELAY_CONTROL_COMPORT_1_OPEN_RETURN = [0xFE, 0x05, 0x00, 0x00, 0xFF, 0x00, 0x98, 0x35]
RELAY_CONTROL_COMPORT_1_CLOSE = [0xFE, 0x05, 0x00, 0x00, 0x00, 0x00, 0xD9, 0xC5]
RELAY_CONTROL_COMPORT_1_CLOSE_RETURN = [0xFE, 0x05, 0x00, 0x00, 0x00, 0x00, 0xD9, 0xC5]
RELAY_CONTROL_COMPORT_2_OPEN = [0xFE, 0x05, 0x00, 0x01, 0xFF, 0x00, 0xC9, 0xF5]
RELAY_CONTROL_COMPORT_2_CLOSE = [0xFE, 0x05, 0x00, 0x01, 0x00, 0x00, 0x88, 0x05]
RELAY_CONTROL_COMPORT_3_OPEN = [0xFE, 0x05, 0x00, 0x02, 0xFF, 0x00, 0x39, 0xF5]
RELAY_CONTROL_COMPORT_3_CLOSE = [0xFE, 0x05, 0x00, 0x02, 0x00, 0x00, 0x78, 0x05]
RELAY_CONTROL_COMPORT_4_OPEN = [0xFE, 0x05, 0x00, 0x03, 0xFF, 0x00, 0x68, 0x35]
RELAY_CONTROL_COMPORT_4_CLOSE = [0xFE, 0x05, 0x00, 0x03, 0x00, 0x00, 0x29, 0xC5]
RELAY_CONTROL_COMPORT_5_OPEN = [0xFE, 0x05, 0x00, 0x04, 0xFF, 0x00, 0xD9, 0xF4]
RELAY_CONTROL_COMPORT_5_CLOSE = [0xFE, 0x05, 0x00, 0x04, 0x00, 0x00, 0x98, 0x04]
RELAY_CONTROL_COMPORT_6_OPEN = [0xFE, 0x05, 0x00, 0x05, 0xFF, 0x00, 0x88, 0x34]
RELAY_CONTROL_COMPORT_6_CLOSE = [0xFE, 0x05, 0x00, 0x05, 0x00, 0x00, 0xC9, 0xC4]
RELAY_CONTROL_COMPORT_7_OPEN = [0xFE, 0x05, 0x00, 0x06, 0xFF, 0x00, 0x78, 0x34]
RELAY_CONTROL_COMPORT_7_CLOSE = [0xFE, 0x05, 0x00, 0x06, 0x00, 0x00, 0x39, 0xC4]
RELAY_CONTROL_COMPORT_8_OPEN = [0xFE, 0x05, 0x00, 0x07, 0xFF, 0x00, 0x29, 0xF4]
RELAY_CONTROL_COMPORT_8_CLOSE = [0xFE, 0x05, 0x00, 0x07, 0x00, 0x00, 0x68, 0x04]
RELAY_CONTROL_COMPORT_9_OPEN = [0xFE, 0x05, 0x00, 0x08, 0xFF, 0x00, 0x19, 0xF7]
RELAY_CONTROL_COMPORT_9_CLOSE = [0xFE, 0x05, 0x00, 0x08, 0x00, 0x00, 0x58, 0x07]
RELAY_CONTROL_COMPORT_10_OPEN = [0xFE, 0x05, 0x00, 0x09, 0xFF, 0x00, 0x48, 0x37]
RELAY_CONTROL_COMPORT_10_CLOSE = [0xFE, 0x05, 0x00, 0x09, 0x00, 0x00, 0x09, 0xC7]
RELAY_CONTROL_COMPORT_11_OPEN = [0xFE, 0x05, 0x00, 0x0A, 0xFF, 0x00, 0xB8, 0x37]
RELAY_CONTROL_COMPORT_11_CLOSE = [0xFE, 0x05, 0x00, 0x0A, 0x00, 0x00, 0xF9, 0xC7]
RELAY_CONTROL_COMPORT_12_OPEN = [0xFE, 0x05, 0x00, 0x0B, 0xFF, 0x00, 0xE9, 0xF7]
RELAY_CONTROL_COMPORT_12_CLOSE = [0xFE, 0x05, 0x00, 0x0B, 0x00, 0x00, 0xA8, 0x07]
RELAY_CONTROL_COMPORT_13_OPEN = [0xFE, 0x05, 0x00, 0x0C, 0xFF, 0x00, 0x58, 0x36]
RELAY_CONTROL_COMPORT_13_CLOSE = [0xFE, 0x05, 0x00, 0x0C, 0x00, 0x00, 0x19, 0xC6]
RELAY_CONTROL_COMPORT_14_OPEN = [0xFE, 0x05, 0x00, 0x0D, 0xFF, 0x00, 0x09, 0xF6]
RELAY_CONTROL_COMPORT_14_CLOSE = [0xFE, 0x05, 0x00, 0x0D, 0x00, 0x00, 0x48, 0x06]
RELAY_CONTROL_COMPORT_15_OPEN = [0xFE, 0x05, 0x00, 0x0E, 0xFF, 0x00, 0xF9, 0xF6]
RELAY_CONTROL_COMPORT_15_CLOSE = [0xFE, 0x05, 0x00, 0x0E, 0x00, 0x00, 0xB8, 0x06]
RELAY_CONTROL_COMPORT_16_OPEN = [0xFE, 0x05, 0x00, 0x0F, 0xFF, 0x00, 0xA8, 0x36]
RELAY_CONTROL_COMPORT_16_CLOSE = [0xFE, 0x05, 0x00, 0x0F, 0x00, 0x00, 0xE9, 0xC6]
