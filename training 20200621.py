# date: 20200622
import pandas as pd
import requests
from bs4 import BeautifulSoup
# 请求URL
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
html=requests.get(url, headers=headers, timeout=10)
content = html.text
# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser')

#分析当前页面的投诉信息
def analysis(soup):

    temp = soup.find('div',class_='tslb_b')
    #创建DataFrame
    df = pd.DataFrame(columns = ['id','brand','car_model','type','desc','problem','datetime','status'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        #提取汽车投诉信息
        temp = {}
        td_list = tr.find_all('td')
        #第一个tr没有td,其余都有8个td
        if len(td_list) > 0:
            id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text,td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            #放到DataFrame中
            temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp[problem], temp['datetime'], temp['status'] = id, brand, car_model, type, desc, problem, datetime, status
            df = df.append(temp, ignore_index=True)
    return

df = analysis(soup)
print(df)