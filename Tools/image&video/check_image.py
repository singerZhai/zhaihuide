import os


class CheckImage():

    def check_image(self, files_path):
        if files_path not in os.listdir(os.path.abspath(os.path.dirname(__file__))):
            print("没有此目录")
            return
        files_list = os.listdir(os.path.abspath(os.path.dirname(__file__)) + "/" + files_path + "/")
        path = os.path.abspath(os.path.dirname(__file__)) + "/" + files_path + "/"
        demo_list = []
        for i in files_list:
            with open(path + i, "rb") as f:
                res = f.read()
                if res == b"":
                    print("损坏文件：%s" % i)
                    demo_list.append(res)
        if b"" not in demo_list:
            print("无损坏文件")
        print("Success!")


if __name__ == '__main__':
    check = CheckImage()
    path = input("path：(*非中文路径)")
    check.check_image(path)
