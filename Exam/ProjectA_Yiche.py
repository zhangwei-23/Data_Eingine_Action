# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 得到页面的内容
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html = requests.get('http://car.bitauto.com/xuanchegongju/?l=8&mid=8', headers=headers, timeout=10)
content = html.text
# 通过content创建BeautifulSoup对象
# soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
soup = BeautifulSoup(content, 'html.parser')

# 分析当前页面数据
temp = soup.find('div', class_='search-result-list')
# 创建DataFrame
df = pd.DataFrame(columns = ['名称', '最低价格', '最高价格', '图片链接'])

search_list = temp.find_all('div', class_='search-result-list-item')

for item in search_list:
    img_path = item.find('img')['src'] #提取图片链接
    # 提取车型名称
    car_model_name = item.find('p', class_="cx-name text-hover").string

    # 提取价格范围
    price_range = item.find('p', class_="cx-price").string
    if price_range == '暂无':
        cheapest_price = '/'
        highest_price = '/'
    else:
        cheapest_price = float(price_range.split('-')[0])
        highest_price = float(price_range.split('-')[1][:-1])

    new_row = {'名称': car_model_name, '最低价格': cheapest_price,
           '最高价格': highest_price, '图片链接': img_path}
    df = df.append(new_row, ignore_index=True)

# 保存数据
df.to_csv('car_price.csv', index=False, encoding='utf_8_sig')





