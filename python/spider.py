from bs4 import BeautifulSoup                          #网页解析，获取数据
import re                           #正则表达式，进行文字匹配
import xlwt                         #进行excel操作
import urllib.request,urllib.error  #制定url，获取网页数据
import sqlite3                      #进行sqlite数据库分析
from urllib import parse
import string
#
# def main():
#     baseurl="https://movie.douban.com/top250?start="
#     #1.爬取网页
#     datalist = Getdata(baseurl)
#     savepath="豆瓣电影.xls"
#     #3.保存数据
#     saveData(datalist,savepath)
#
# #影片详情链接的规则
# findLink=re.compile(r'<a href="(.*?)">')           #创建正则表达式对象，表示规则（字符串的模式）
# #影片图片链接的规则
# findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)   #re.S换行符包含在字符中
# #影片片名
# findTitle = re.compile(r'<span class="title">(.*)</span>')
# #影片评分
# findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# #评价人数
# findpeople=re.compile(r'<span>(\d*)人评价</span>')
# #找到概况
# findInq=re.compile(r'<span class="inq">(.*)</span>')
# #找到影片的相关内容
# findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
#
#
# #1.爬取网页
# def Getdata(baseurl):
#     datalist=[]
#     for i in range(0,1):
#         url = baseurl + str(i*25)
#         html = askUrl(url)              #保存获取的网页源码
#
#         # #2.逐一解析数据
#         soup = BeautifulSoup(html,"html.parser")
#         for item in soup.find_all('div',class_="item"):#查找符合要求的字符串，形成列表
#             # print(item)       #测试：查看电影item的全部信息
#             data=[]             #保存一部电影的全部信息
#             item=str(item)
#
#             #影片详情的超链接
#             link=re.findall(findLink,item)[0]       #re库用来通过正则表达式查找指定的字符串
#             data.append(link)
#
#             imgSrc = re.findall(findImgSrc,item)[0]
#             data.append(imgSrc)
#
#             title=re.findall(findTitle,item)        #片名可能只有中文名
#             if(len(title) == 2):
#                 ctitle = title[0]
#                 data.append(ctitle)
#                 otitle=title[1].replace("/",'') #去掉无关符号
#                 data.append(otitle)
#             else:
#                 data.append(title[0])
#                 data.append(' ')                #外国名留空
#
#             rating=re.findall(findRating,item)[0]
#             data.append(rating)
#
#             people=re.findall(findpeople,item)[0]
#             data.append(people)
#
#             Inq=re.findall(findInq,item)
#             if len(Inq)!=0:
#                 Inq = Inq[0].replace(".","")
#                 data.append(Inq)                       #添加概述
#             else:
#                 data.append(" ")
#
#             bd=re.findall(findBd,item)[0]
#             bd=re.sub("<br(\s+)?/>(\s+)?"," ",bd)   #去掉<br/>
#             bd=re.sub('/'," ",bd)   #替换/
#             data.append(bd.strip()) #去掉前后的空格
#
#             datalist.append(data)           #把处理好的一部电影信息加入datalist
#
#
#
#     return datalist
#
# #得到指定一个url的网页内容
# def askUrl(url):
#     head = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"
#     }
#     url=parse.quote(url,safe=string.printable)
#     request = urllib.request.Request(url,headers=head)
#     html=""
#     try:
#         response = urllib.request.urlopen(request)
#         html=response.read().decode("utf-8")
#         # print(bs.find_all(re.compile("a")))
#         # print(bs.find_all("a"))
#         # print(html)
#     except urllib.error.URLError as e:
#         if hasattr(e,"code"):
#             print(e.code)
#         if hasattr(e,"reason"):
#             print(e.reason)
#     return html
#
#
#
# #3.保存数据
# def saveData(datalist,savepath):
#     book=xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
#     sheet=book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)  #创建工作表
#     col = ("电影详情链接", "图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
#     print("save....")
#     for i in range(8):
#         sheet.write(0,i,col[i])   #列名
#     for i in range(100):
#         print("第%d条"%i)
#         data=datalist[i]
#         for j in range(0,8):
#             sheet.write(i+1,j,data[j])
#
#     book.save(savepath)
#
# if __name__ == "__main__":
#     main()
#     print("爬取成功！")



def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1. 爬取网页
    datalist = Getdata(baseurl)
    savepath = "豆瓣电影.xls"
    # 3. 保存数据
    saveData(datalist, savepath)

#影片详情链接的规则
findLink=re.compile(r'<a href="(.*?)">')           #创建正则表达式对象，表示规则（字符串的模式）
#影片图片链接的规则
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)   #re.S换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findpeople=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)

# 1. 爬取网页
def Getdata(baseurl):
    datalist = []
    for i in range(0, 4):  # 爬取前4页，每页25条，共100条
        url = baseurl + str(i * 25)  # 每页间隔25个项目
        html = askUrl(url)  # 保存获取的网页源码

        # 2. 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            data = []  # 保存一部电影的全部信息
            item = str(item)

            # 影片详情的超链接
            link = re.findall(findLink, item)[0]
            data.append(link)

            # 影片图片链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            # 影片片名
            title = re.findall(findTitle, item)
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("/", '')  # 去掉无关符号
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')  # 外国名留空

            # 影片评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            # 评价人数
            people = re.findall(findpeople, item)[0]
            data.append(people)

            # 概况
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace(".", "")
                data.append(inq)  # 添加概述
            else:
                data.append(" ")

            # 相关信息
            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影信息加入datalist

    return datalist

#得到指定一个url的网页内容
def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"
    }
    url=parse.quote(url,safe=string.printable)
    request = urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(bs.find_all(re.compile("a")))
        # print(bs.find_all("a"))
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

# 3. 保存数据
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    print("save....")
    for i in range(8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(len(datalist)):  # 修改为遍历所有爬取到的电影数据
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)

if __name__ == "__main__":
    main()
    print("爬取成功！")
