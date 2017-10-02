#!/usr/bin/env python

import requests, time, os.path, sys, pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient
from multiprocessing import process

client = pymongo.MongoClient('localhost', 27017)
pig = client['Pig']
second_info = pig['third_info_bj']


# req = requests.get('http://58.240.51.118/getPassword_cu.jsp?command=getpassword&phonenumber=jsltlanschool_18652961653&t=0.5308168062467711')
# soup = BeautifulSoup(req.text,'lxml')
# print(soup.get_text)



class Spider(object):
    def __init__(self):
        pass

    def get_sex(self, content):
        if content == ['member_ico1']:
            return '女'
        elif content == ['member_ico']:
            return '男'
        else:
            return '未知'

    def get_each_index_url(self, area):
        for x in range(1, 21):
            full_url = 'http://{}.xiaozhu.com/search-duanzufang-p{}-0/'.format(area, x)
            req = requests.get(full_url)
            soup = BeautifulSoup(req.text, 'lxml')
            links = soup.select('#page_list > ul > li > a')
            for i in links:
                link = i.get('href')
                self.get_detail_info(link)
                # print(link)

    def get_detail_info(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        titles = soup.select('div.con_l > div.pho_info > h4 > em')
        addresss = soup.select('div.con_l > div.pho_info > p > span')
        prices = soup.select('#pricePart > div.day_l > span')
        landlords = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
        sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
        detail_url = url

        for title, address, price, landlord, sexx in zip(titles, addresss, prices, landlords, sexs):
            t = title.get_text()
            a = address.get_text().rstrip()
            p = price.get_text()
            l_url = landlord.get('href')
            l_name = landlord.get_text()
            sex = self.get_sex(sexx.get('class'))
            data = {
                'tittle': t,
                'address': a,
                'price': p,
                'landlord_url': l_url,
                'lanlord_name': l_name,
                'sex': sex,
                'detail_url': detail_url
            }
            second_info.insert_one(data)
            # print(data)
            for _ in second_info.find():
                print(_)


if __name__ == '__main__':
    area = input('Please enter the city you want to query (just like that 北京 = bj or 南京 = nj):')
    s = Spider().get_each_index_url(area)
    # f = s

print('All infos load complete!')



'http://ditu.amap.com/search?query='
