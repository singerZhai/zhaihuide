import os
import requests
import json
import base64
from hashlib import md5
import time
import sys
from PIL import Image
import cv2

# # def base64_photo(photo_path):
# #     with open(photo_path, "rb") as f:
# #         res = base64.b64encode(f.read())
# #     return res
# #
# #
# headers = {
#     "Connection": "keep-alive",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#     "Referer": "https://blog.csdn.net/kdapi/article/details/53415611",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
# }
#
# session = requests.session()
# session.keep_alive = False  # Max retries exceeded with url 错误，及时关闭http连接
#
# res = base64.b64encode("翟会德".encode("utf-8"))
# # print(res)
# id_num = "130221199510297119"
# id_num_md5 = md5(id_num.encode("UTF-8")).hexdigest()
#
# url1 = "http://10.94.181.54:8010/risk/api/living/h5/checkclientinfo"
# data1 = {
#     "sp_no": "1000000001",
#     "scene": "loan",
#     "redirect_uri_suc": "http://www.baidu.com",
#     "redirect_uri_fail": "http://www.qq.com",
#     "index": "0",
#     "file_type": "image",
#     "skin": "1",
#     "name": res,
#     "id_no": id_num_md5
# }
#
# r1 = session.post(url=url1, data=data1, headers=headers)
# res1 = r1.json()
# # print(res1)
#
# session_key = res1["result"]["session_key"]
# url2 = "http://10.94.181.54:8010/risk/api/living/h5/getidlcode?session_key=" + session_key + "&sp_no=1000000001"
# r2 = session.get(url2)
# print(r2.json())


# img = Image.open("drivecarddetection.jpg")
# print(img.size)
#
# out = img.resize((10, 5))
#
# out.save("idcard_back_error.jpg")
# demo = sys.argv[0]
# print(demo)


# img = Image.open("bankcard2.jpg")
# print(img.size)
#
# out = img.resize((3000, 3000))
#
# out.save("bankcard2_error.jpg")


# img = cv2.imread("bankcard2.jpg", 0)
# cv2.imshow("image", img)
# size = img.shape  # 获取图片大小（长，宽，通道数）
# tempimg = cv2.resize(img, (size[1] * 10, size[0] * 8), cv2.INTER_LINEAR)
# cv2.imwrite("bankcard2_error.jpg", tempimg)
# cv2.imshow("imag2", tempimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


url = "http://10.94.181.54:8010/risk/token/generate"
headers = {
    "Host": "10.94.181.54:8010",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "BDRIM-1.9.0.0-Android-1000000002_1080_1920_MIX-lithium_23_6.0.1_1.0_1",
}

data = {
    "datetime": int(time.time()),
    "encode": "utf-8",
    # "ua": "BDRIM-1.9.0.0-Android-1000000002_1080_1920_MIX-lithium_23_6.0.1_1.0_1",
    "ua": "BDRIM-1.0.0-IOS-Channel_750_1334_iphone_10.3.1_10.3.1_1.0_1",
    "appid": "CCgAAAAAAAADkoKfeZCLnLD1dHttvia3Z",
    "wcp": "eyJjdWlkXzIiOiJNQUFBQUFBQUFBQUdiTzRaZUtVaVRlQm9yWDJIOW80T2NISThlQ3pjcVdWQ2VEaTVqZEtjY3FhZk0yT1FRRDFYenB3aTdLNGxySHJ0V0c5OWJGTCtzYTBkZEpzUDhnVFAiLCJma193Y3AiOiJTd0FBQUFBQUFBQ05kVG10cnNnM29EZlNcL2MxM2ZmNW5mYlI4SXlJUDRsSVwvM1c0NHpZZGMyTGJ6VXRFVnNvNGVyTFFhRXdiMTlld0dldGpRVFU1TnJcLzFpSE5uRnJ3TURXb0ZkazRnU3IxSWU4cXQzRUdBRHp3PT0iLCJuZXR0eXBlIjoiQVFBQUFBQUFBQUNCTmFLbW5PcHVLRzNybGN1dTNTMTEiLCJ3aW1laSI6IkR3QUFBQUFBQUFBcnNiWDJSZkNXVWtsTlVQOVRiVERSWWFxNkRYUEdKVTNFcitmd1RZS1lmZz09Iiwid21pcCI6IkRnQUFBQUFBQUFEV1ZZRGdyQ2VRWGU2dnZLVnlkR2hpIiwid2xvYyI6IiIsIndpbXNpIjoiIiwid3NzbiI6IiIsIndwbiI6IiIsIndzc2lkIjoiSUFBQUFBQUFBQUR5RmNZUmNhQTFMMjU2SHFcL0tUT3VBU0lmRlwvV2dKbm9Ic1FBdG8zVG1lcjRSZzlnaDJwWEVvMlZqYmJHRVJ2NEk9In0=",
    "key": "nOx6fBl0xUHNQdDnizAinQ3ERG6SPhYxOc8X+/RqaEMzElp+wFoPVs/SuOCkLCRbnGTym42i41XYQszPRGPszv2hpVCwNZEPBVnVy6x2pdRk9E2qSZNOQLu57GkhrGXsK6dUawzw68RFF0tAgXn+4WHcrSlQA9N7fgXe/cBjmiSksjdZ5tB+wqhDc8B2JlFsY/iJIAdzZqDSA7diwGK7Tui2B9sj7pLeHIdr5oXOq/syf+3sjxQkSdpdE7Gb+GYikUURTZo0i2OIj/9Fb+VtXyksfRWKyKvfwV6aSepsI8UCs5vWDTx9lWcQX0FWO5sjy44upNZRES7aXpaFcCI1ig==",
    "reqid": "IAAAAAAAAACCmNRBg5uTfImn7FfkKAJqpvk7WeqMUxjCg55J0Z7XuET8b/+hlWcbRAP2HFdFwqY=",
    "sp_params": "IAAAAAAAAAA9D6Gsr/TIwT9QIIWelo4cqcfvxRJEYzh4EL6lFCn3FLOMnpD1GzxGATymko99LDs=",
    # "s1": "KAAAAAAAAABG15I9qkhw/to4AkABMPVuBSoT/D106aD21OoYwSQSq2UleXmwI55CjQHyEFPgtV0=",
    "nonce": "IAAAAAAAAABAfSiy9Cu9v1/Wh4uWEiySIqWZFB4mNShpi/7Jg/g4vw1g62RYVk3k8suX2HsmkTY=",

}
# print(data)
r = requests.post(url=url, data=data)
print(r.headers)
print(r.status_code)
print(r.text)