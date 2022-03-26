# coding = utf8
import os

import numpy as np
import openpyxl
import pandas as pd

os.path.abspath(".")
"""
    @Project:pythonProject_seevision
    @File:digitalZoomTestCase.py
    @Author:十二点前要睡觉
    @Date:2022/3/23 10:33
    @Description:自动化测试点分解：（每次测试操作 + 一次串口log获取操作 = 完整的操作）
        1、6个分辨率：
            MJPG 3840*2160
            MJPG 1920*1080
            MJPG 1280*720
            H264 3840*2160
            H264 1920*1080
            H264 1280*720
        2、测试点：
            a、错误值：
                无缩放状态->缩小1step  
                    [1、弹框操作失败，2、zoom: 1, step 1]
                无缩放状态->过度放大53step   
                    [1、弹框操作失败，2、zoom: 0, step 53]
                放大40step状态->过度缩小53step
                    [1、zoom: 0, step 40，2、x: 1280, y: 720, w: 1280, h: 720]
            b、有效值：
                放大->右移动画面1step：
                    放大5step
                        [1、zoom: 0, step 5，2、x: 160, y: 90, w: 3520, h: 1980，3、direction: 3, step 1，4、x: 192, y: 90]
                        规律： -- important
                            (通过w、h、x、y来判断放大、缩小、移动的值是否正确)
                            所有分辨率的放大缩小移动都是以4K的进行的
                            1、放大的公式：w=w1-step*64，h=h1-step*36
                            2、缩小的公式：w=w1+step*64，h=h1+step*36
                            3、右移动的公式：x=x1+step*32, y=y1
                    放大10step
                    放大14step
                    放大17step
                    放大20step
                    放大23step
                    放大25step
                    放大27step
                    放大28step
                    放大30step
                    放大31step
                    放大33step
                    放大34step
                    放大35step
                    放大36step
                    放大37step
                    放大38step
                    放大39step
                    放大40step
                放大40step->缩小->右移动画面1step：
                    缩小1step
                        [1、zoom: 0, step 40，2、x: 1280, y: 720, w: 1280, h: 720，3、zoom: 1, step 1，4、x: 1248, y: 702, w: 1344, h: 756，5、direction: 3, step 1，6、x: 1280, y: 702]
                    缩小2step
                        [1、]
                    缩小3step
                        [1、]
                    缩小4step
                        [1、]
                    缩小5step
                        [1、]
                    缩小6step
                        [1、]
                    缩小7step
                        [1、]
                    缩小9step
                        [1、]
                    缩小10step
                        [1、]
                    缩小12step
                        [1、]
                    缩小13step
                        [1、]
                    缩小15step
                        [1、]
                    缩小18step
                        [1、]
                    缩小20step
                        [1、]
                    缩小23step
                        [1、]
                    缩小26step
                        [1、]
                    缩小30step
                        [1、]
                    缩小35step
                        [1、]
                    缩小40step
                        [1、]
"""


# 从excel中读取数据并返回（element）
def read_excel_for_page_element(form="./doc/数码变焦测试用例V2.0.xlsx", sheet_name="数码变焦case自动化部分"):
    df = pd.read_excel(form, sheet_name=sheet_name, index_col="测试分辨率", engine="openpyxl")
    # original_data = df.loc[1, "测试点"]
    test_case_list = []
    for i in range(1, df.shape[0]):
        original_data = df.loc[i, "测试点"]
        test_case_list.append([i, original_data])
    return test_case_list


def write_into_excel(form="./doc/数码变焦测试用例V2.0.xlsx", sheet_name="数码变焦case自动化部分", row=1, column=1):
    wb = openpyxl.load_workbook(form)
    ws = wb[sheet_name]
    ws.cell(row + 1, column).value = "PASS"
    wb.save(form)


if __name__ == '__main__':
    # print(read_excel_for_page_element()[0])
    row = read_excel_for_page_element()[5][0]
    write_into_excel(row=row, column=7)
