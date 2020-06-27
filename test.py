#coding utf-8

# import re
# from bs4 import BeautifulSoup
# import urllib.request,urllib.error
# import xlwt
# import sqlite3

#
# def main():
#     baseurl = "https://movie.douban.com/top250"
#     #1 爬取网页
#     datalist = getData(baseurl)
#     savepath= ".\\豆瓣电影Top250.xls"
#     #3 保存数据
#     saveData(savepath)
#
#  #1 爬取网页
# def getData(baseurl):
#     datalist = []
#     # 2 逐一解析数据
#     return datalist
#
# #3 保存数据
# def saveData(savepath):
#     prin('...')

import urllib.request
response = urllib.request.urlopen("https://www.baidu.com")
print(response.read().decode('utf-8'))




