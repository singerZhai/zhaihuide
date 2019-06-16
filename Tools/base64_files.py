import base64
from hashlib import md5
import os


# 加密文件  base64  md5
class Util(object):

    # 文件 base64得公共方法
    @staticmethod
    def __filesBase64(ImageVideoName, fileName):
        with open(ImageVideoName, 'rb') as f:
            data = base64.b64encode(f.read())
            with open(fileName + ".txt", 'wb') as a:
                a.write(data)

    # base64加密 image
    def imageBase64(self):
        imageName = input("image_name：(*包含文件后缀名)")
        if imageName == "all":
            fileList = list()
            for i in os.listdir(os.path.abspath(os.path.dirname(__file__))):
                if i.endswith(".jpg") or i.endswith(".png"):
                    fileList.append(i)
            for i in fileList:
                self.__filesBase64(i, i)
            print("all success")
            return
        path = os.path.abspath(os.path.dirname(__file__)) + "/" + imageName
        if not os.path.exists(path):
            print("请在 %s 目录下添加 .jpg 文件" % os.path.abspath(os.path.dirname(__file__)))
            return
        fileName = input("file_name：")
        self.__filesBase64(imageName, fileName)
        print("success")

    # base64加密 video
    def videoBase64(self):
        videoName = input("video_name：(*包含文件后缀名)")
        path = os.path.abspath(os.path.dirname(__file__)) + "/" + videoName
        if not os.path.exists(path):
            print("请在 %s 目录下添加 .mp4 文件" % os.path.abspath(os.path.dirname(__file__)))
            return
        self.__filesBase64(videoName, videoName)
        print("success")

    # md5加密 string
    @staticmethod
    def encrypt_md5(str):
        # 创建md5对象
        new_md5 = md5()
        # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
        new_md5.update(str.encode(encoding='utf-8'))
        # 加密
        print("result：" + new_md5.hexdigest())


if __name__ == '__main__':
    util = Util()
    while True:
        doingNum = input("请输入操作：1(base64_image) 2(base64_video) 3(md5_string)")
        if doingNum == "1":
            util.imageBase64()
            break
        elif doingNum == "2":
            util.videoBase64()
            break
        elif doingNum == "3":
            str = input("string：")
            util.encrypt_md5(str)
            break
        else:
            print("输入有误")
            continue
