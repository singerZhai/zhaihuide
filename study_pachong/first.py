# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-14 13:27
# @File    : first.py
# @Software: PyCharm
# coding=utf-8
from urllib import request, error, robotparser
import urllib
import ssl
import re
import itertools
from urllib.parse import urljoin

pa = re.compile(r'(?<=>)[^<>]+(?=<)')

ssl._create_default_https_context = ssl._create_unverified_context
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"


def download(url, user_agent=user_agent, count=2):
    print("Download: ", url)
    headers = {"User-agent": user_agent}
    req = request.Request(url, headers=headers)
    try:
        html = request.urlopen(req).read().decode("utf-8")
    except error.HTTPError as e:
        print("Download error: ", e.reason)
        html = None
        if count > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, count - 1)
    return html


def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        rp = robotparser.can_fetch()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    web_page_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',
                                re.IGNORECASE)
    return web_page_regex.findall(html)


print(link_crawler("http://example.webscraping.com", "/(index|view)"))
