# -*- coding: utf-8 -*-
import requests
import csv
import time
from bs4 import BeautifulSoup
def get_content(url,data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.body.find('div',{'class':'mach_list2'})
    data_list = soup.find_all('dl')
    infos = []
    print(data_list)
    for rows in data_list:
        try:
            company = rows.find('h4').find('a')['title']
            phone = rows.find('span').find('a').string
        except:
            continue
        infos.append([company, phone])
        print(company,phone)
    return infos
# 生成文件
def write_data(data,name):
    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["company", "phone"])
        for d in data:
            writer.writerow([d[0], d[1]])
    print('抓取完成')
# 导出文件

if __name__ == '__main__':
    url = 'http://b2b.huangye88.com/zhengzhou/huagong/'
    # url = "https://www.baidu.com"
    mydata = get_content(url)
    write_data(mydata, 'phone.csv')