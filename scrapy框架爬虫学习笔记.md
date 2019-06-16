##   scrapy框架爬虫学习笔记

###   1.创建scrapy项目

- scrapy startproject 项目名称

###   2.创建spider爬虫

- Scrapy genspider ...spider(爬虫名) 爬取的网站主页面的URL(www.baidu.com)

###   3.各个文件作用

- items
  - 创建类，类中属性为最后数据的字段名
- middlewares
  - 添加两个类：代理 & userAgent  list
- pipelines
  - 定义每个爬虫的pipeline类
- settings
  - scrapy的相关配置

###   4.运行项目并取得scv或json数据

- 命令：scrapy crawl ...spider(爬虫名) -o 自定义文件名.csv 或者json

