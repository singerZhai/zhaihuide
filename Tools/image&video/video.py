import cv2
import os


class Util(object):

    def __filesPath(self):
        self.path = os.listdir(str(os.path.abspath(os.path.dirname(__file__))) + "/video/")
        self.demo_list = list()
        for i in self.path:
            if i.endswith(".mp4") or i.endswith(".MOV"):
                self.demo_list.append(i)
        return self.demo_list

    def demo(self):
        timeF = 5
        count = 1
        for i in self.__filesPath():
            video = cv2.VideoCapture("video/" + i)
            c = 1
            if video.isOpened():
                rval, frame = video.read()
            else:
                rval = False
            while rval:
                rval, frame = video.read()
                if c % timeF == 0:
                    imagePath1 = os.path.abspath(os.path.dirname(__file__))
                    imagePath = imagePath1 + "/"
                    resImagePath = imagePath + "image/"
                    if not os.path.exists(resImagePath):
                        os.mkdir(resImagePath)
                    cv2.imwrite(resImagePath + str(count) + ".jpg", frame)
                    count += 1
                c += 1
                cv2.waitKey(1)
            video.release()

    @staticmethod
    def files_count():
        path = os.listdir(os.path.abspath(os.path.dirname(__file__)) + "/image/")
        files_count = len(path)
        print("files_count is %d" % files_count)


if __name__ == '__main__':
    util = Util()
    util.demo()
    util.files_count()
