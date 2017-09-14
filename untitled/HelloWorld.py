#coding=utf-8
import urllib
import re
import sys

# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# html = getHtml("http://www.12999.com/html2/10868.html")
#
# print html


# 正则表达式获取文件ID
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
#
# def getnub(html):
#     reg = r'href=\'/page/\d\d-\d\d-\d\d/(.+?).html'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html)
#     return imglist
#
#
# html = getHtml("http://www.12999.com/html2/10864.html")
# print getnub(html)

#测试
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
#
# def getnub(html):
#     reg = r'<title>(.+)</title>'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html)
#     return imglist
#
#
# html = getHtml("http://www.12999.com/html2/10864.html")
# print getnub(html)

