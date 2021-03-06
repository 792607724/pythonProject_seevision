# coding = utf8
import csv
import logging
import multiprocessing
import os
import subprocess
import sys

os.path.abspath(".")
__author__ = "CHENGUANGTAO"

from airtest.core.api import *
from PIL import Image
import imagehash

auto_setup(__file__)
cur_time = time.strftime("%Y%m%d_%H%M%S")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 过滤airtest log只打印ERROR的Log
logger_airtest = logging.getLogger("airtest")
logger_airtest.setLevel(logging.ERROR)

"""
    考虑到adb连接问题，当前测试使用adb wifi模式连接，框架中有关adb调用，如device.stop_app()\device.start_app()均不能使用，需要使用其他方法兼容
"""


def init_Device(serialno="7c2440fd"):
    device = connect_device("android:///{}?cap_method=javacap&touch_method=adb".format(serialno))
    poco = AndroidUiautomationPoco(device, use_airtest_input=True, screenshot_each_action=False)
    return poco, device


def stress_test(device, poco, test_times=1000):
    cur_test_app = "com.tawuyun.storecenter"
    i = 1
    csv_result = []
    try:
        for i in range(i, test_times):
            # device.start_app(cur_test_app)
            sleep(3)
            poco(text="它物云门店").wait().click()
            sleep(2)
            poco(text=">>模拟采集").wait().click()
            sleep(2)
            poco(text="激活").wait().click()
            sleep(2)
            poco(text="开始采集").wait().click()
            sleep(8)
            if poco(text="OK").wait().exists():
                poco(text="OK").wait().click()
                sleep(3)
            if poco(text="OK").wait().exists():
                poco(text="OK").wait().click()
                sleep(3)
            test_result = assert_exists(Template(r"tpl1629811182456.png", record_pos=(0.178, 0.102), resolution=(1640, 720)), "请填写测试点")
            print("Test times is：{} -- Check whether picture exists and result is {}".format(str(i), test_result))
            csv_result.append([i, cur_time, test_result])
            sleep(3)
            device.keyevent("BACK")
            sleep(2)
            device.keyevent("BACK")
            sleep(2)
            device.keyevent("BACK")
            sleep(2)
    except Exception as ex:
        print("Current test is happened error, please check and error code is :{}".format(str(ex)))
    finally:
        result_calculate(data=csv_result)
        sys.exit(0)



def launchCameraTest(device, poco):
    for i in range(100):
        sleep(3)
        poco(text="相机").wait().click()
        sleep(3)
        device.keyevent("BACK")
        sleep(3)
        print("This is {} times test".format(i + 1))


def stress_webcam_test(device, poco, test_times=1000):
    cur_test_app = "com.webcamhostapp.app"
    i = 1
    csv_result = []
    try:
        for i in range(i, test_times):
            sleep(3)
            poco(text="WebCamHostApp").click()
            sleep(3)
            if poco(text="OK").wait().exists():
                poco(text="OK").wait().click()
                sleep(3)
            if poco(text="OK").wait().exists():
                poco(text="OK").wait().click()
                sleep(3)
            sleep(5)
            test_result = exists(Template(r"tpl1628944649838.png", record_pos=(-0.015, -0.426), resolution=(720, 1640)))
            print("Test times is：{} -- Check whether picture exists and result is {}".format(str(i), test_result))
            csv_result.append([i, cur_time, test_result])
            sleep(1)
            device.keyevent("BACK")

    except Exception as ex:
        print("Current test is happened error, please check and error code is :{}".format(str(ex)))
    finally:
        result_calculate(data=csv_result)
        sys.exit(0)


def check_image_quality(device, poco, test_times=1000):
    i = 1
    csv_result = []
    try:
        for i in range(i, test_times):
            sleep(3)
            poco(text="它物云门店").wait().click()
            sleep(2)
            poco(text=">>模拟采集").wait().click()
            sleep(2)
            poco(text="激活").wait().click()
            sleep(2)

            poco(text="开始采集").wait().click()
            sleep(5)
            if poco(text="OK").wait().exists():
                poco(text="OK").wait().click()
                sleep(3)
            if poco(text="OK").wait().exists():
                poco(text="OK").wait().click()
                sleep(3)
            # 截图
            file_name = "./screenshot/{}.jpg".format(str(i))
            snapshot(filename = file_name)
            sleep(3)
            normal_picture = imagehash.average_hash(Image.open("./normal_picture.jpg"))
            screenshot_picture = imagehash.average_hash(Image.open(file_name))
            if normal_picture == screenshot_picture:
                test_result = "Same picture {}".format(str(i))
            else:
                test_result = "Different picture {}".format(str(i))
                break
            print("Test times is：{} -- result is {}".format(str(i), test_result))
            csv_result.append([i, cur_time, test_result])
            sleep(3)
            device.keyevent("BACK")
            sleep(2)
            device.keyevent("BACK")
            sleep(2)
            device.keyevent("BACK")
            sleep(2)
    except Exception as ex:
        print("Current test is happened error, please check and error code is :{}".format(str(ex)))
    finally:
        result_calculate(data=csv_result)
        sys.exit(0)


def log_process():
    subprocess.Popen("adb -s 192.168.50.109:5555 shell logcat -b all>./stress_test.log", shell=True).communicate()[0]


def result_calculate(data=[["1", "2", "3"], "1", "2", "3"], form_name="result.csv"):
    with open("./{}".format(form_name), "w", encoding="utf-8-sig") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["测试次数", "测试时间", "结果"])
        # 取出再写入
        for item in data:
            csv_writer.writerow(item)


if __name__ == '__main__':
    # init_item = init_Device(serialno="192.168.50.109:5555")
    # init_item = init_Device(serialno="192.168.50.187:5555")
    # init_item = init_Device(serialno="192.168.50.168:5555")
    # init_item = init_Device(serialno="192.168.50.107:5555")
    init_item = init_Device(serialno="1f56d837")
    device = init_item[1]
    poco = init_item[0]

    test_pool = multiprocessing.Pool(2)
    # test_pool.apply_async(func=stress_test(device, poco, 101))
    # test_pool.apply_async(func=check_image_quality(device, poco, 30))
    # test_pool.apply_async(func=log_process)
    test_pool.apply_async(func=launchCameraTest(device, poco))

    test_pool.close()
    test_pool.join()
