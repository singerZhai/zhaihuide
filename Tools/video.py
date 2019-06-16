import cv2
import os


# 视频抽帧方法
def demo(Name):
    timeF = 5
    video = cv2.VideoCapture("video/" + str(Name) + ".mp4")
    c = 1
    if video.isOpened():
        rval, frame = video.read()
    else:
        rval = False
    count = 1
    while rval:
        rval, frame = video.read()
        if c % timeF == 0:
            imagePath1 = os.path.dirname(__file__)
            imagePath = imagePath1 + "/"
            resImagePath = imagePath + "image" + str(Name)
            if not os.path.exists(resImagePath):
                os.mkdir(resImagePath)
            cv2.imwrite(resImagePath + "/" + str(count) + ".jpg", frame)
            count += 1
        c += 1
        cv2.waitKey(1)
    video.release()


if __name__ == '__main__':
    name = 1
    while name <= 28:
        demo(name)
        name += 1
