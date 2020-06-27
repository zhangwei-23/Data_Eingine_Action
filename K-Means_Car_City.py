
# coding: utf-8
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing

# 数据加载
data = pd.read_csv(r'D:\Learning\Data Engine\Data_Engine_with_Python-master\L3/car_data.csv', encoding="gbk")
# print(data)

train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]
# print(train_x)

# 聚类成4类
kmeans = KMeans(n_clusters=4)

# 规范化到[0,1]空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# print(train_x)

# 使用kmeans进行聚类
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
print(predict_y)

# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)), axis=1)
result.rename({0:u'聚类结果'}, axis=1, inplace=True)
print(result)

# 将结果导出到CSV文件中
result.to_csv("Car_City_cluster_result.csv", encoding="utf-8-sig",index=False)

