# coding = utf8
import os

os.path.abspath(".")
import pytesseract
from PIL import Image

"""
    @Project:PycharmProjects
    @File:readNumberFromPictrure.py
    @Author:十二点前要睡觉
    @Date:2022/1/6 11:48
"""


class ReadNumberFromPicture:

    def __int__(self):
        pass

    def OCR_Model(self, path=""):
        """
        pytesseract OCR文字识别模块
        :param path:传入待读取的图片路径
        :return:返回读取并处理过的时间
        """
        # img = cv.imread(path)
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(Image.open(path), lang="eng", config="--psm 8")
        # text = pytesseract.image_to_string(gray, lang="eng", config="--psm 8")
        return text

    def readPicture(self, imgPath):
        """
        读取图片上的秒表时间文字信息
        :param imgPath:传入待读取的图片路径
        :return:返回读取并处理过的时间
        """
        c_read_string = self.OCR_Model(path=imgPath).replace("\n", "").strip().replace(" ", "")
        # print(c_read_string)
        # print("\n seperate line \n")
        return c_read_string


if __name__ == '__main__':
    # camera_imgPath = r"D:\PycharmProjects\pythonProject_seevision\windows_control\PerformanceTestScript\Sample\grab_image\camera_grab_00009.jpg"
    # camera_imgPath =r"D:\PycharmProjects\pythonProject_seevision\windows_control\PerformanceTestScript\Sample\MJPEG1080P_NORMALMODE\xxx_00010.jpg"
    # windows_imgPath = r"D:\PycharmProjects\pythonProject_seevision\windows_control\PerformanceTestScript\Sample\grab_image\windows_grab_00009.jpg"
    rnfp = ReadNumberFromPicture()
    # dirPath = r"D:\PycharmProjects\pythonProject_seevision\windows_control\temp\ocr_identifyDir\\"
    dirPath = r"D:\PycharmProjects\pythonProject_seevision\windows_control\PerformanceTestScript\Sample\grab_image\\"
    for imageName in os.listdir(dirPath):
        if imageName.endswith(".jpg"):
            print(rnfp.readPicture("{}{}".format(dirPath, imageName)))
    # print(rnfp.readPicture(windows_imgPath))
