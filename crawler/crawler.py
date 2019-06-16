import time
import random
import requests
import config
import ssl
from lxml import etree

ssl._create_default_https_context = ssl._create_unverified_context

get_url = lambda x: "https://www.zhipin.com/c101010100/?query=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={}&ka=page-{}".format(x, x)

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": config.agents,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": config.cookie
}

proxies = {
    "http": "101.200.50.18:8118",
    "https": "101.200.50.18:8118"
}

boss_url = "https://www.zhipin.com/job_detail/?query=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101010100&industry=&position="


def crawler():
    for i in range(1, 11):
        try:
            response = requests.get(url=get_url(i), headers=headers)
            html = response.text
            # print(html)
            html = etree.HTML(html)
            print("正在爬取第{}页数据".format(i))
            job_name_list = html.xpath("//*[@class='info-primary']//h3//a//div[@class='job-title']/text()")
            job_money_list = html.xpath("//*[@class='info-primary']//h3[@class='name']//a//span/text()")
            company_list = html.xpath(
                "//*[@class='info-company']//div[@class='company-text']//h3[@class='name']//a/text()")
            company_people_count_list = html.xpath("//*[@class='company-text']//p/text()[3]")
            print(job_name_list)
            if len(job_name_list) == 0:
                print("None")
                break
            for a, b, c, d in zip(job_name_list, job_money_list, company_list, company_people_count_list):
                result = "职位名称：{}, 薪资：{}, 公司：{}, 人数：{}\n".format(a, b, c, d)
                print(result)
                f = open("./job_qa.txt", "a+", encoding="utf-8")
                f.write(result)
            f.close()
        except Exception:
            print("请求失败")
            break
        time.sleep(random.random() * 3)


crawler()
