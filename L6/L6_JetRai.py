# coding utf-8
# by ZhangWei

import pandas as pd
from fbprophet import Prophet
from matplotlib import pyplot as plt

# 导入数据
train = pd.read_csv("train.csv")
# print(train.head(5))

# 转换日期格式
train["Datetime"] = pd.to_datetime(train.Datetime, format="%d-%m-%Y %H:%M")
train.index = train.Datetime
# print(train.head(5))

# 去掉“ID”，“Datetime"字段
train.drop(["ID", "Datetime"], axis = 1, inplace = True)
# print(train.head)

# 按天进行采样
daily_train = train.resample('D').sum()
# print(daily_train.head)
daily_train["ds"] = daily_train.index
daily_train["y"] = daily_train.Count
# print(daily_train.head)
daily_train.drop(["Count"], axis = 1, inplace = True)
# print(daily_train)

# 拟合prophet模型
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)
# 预测未来7个月
future = m.make_future_dataframe(periods = 210)
forecast = m.predict(future)
print(forecast)

if __name__ == '__main__':
    m.plot(forecast)
    m.plot_components(forecast)
