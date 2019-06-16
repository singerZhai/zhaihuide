import requests
from lxml import etree


url = "https://so.biqusoso.com/s.php?ie=utf-8&siteid=biqiuge.com&q={}"
response = requests.get(url.format("神级龙卫"))
html = etree.HTML(response.text)
book_list = html.xpath("")