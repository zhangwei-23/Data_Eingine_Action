import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing

# 数据加载
data = pd.read_csv(r'D:\Learning\Data Engine\Data_Engine_with_Python-master\L3/Mall_Customers.csv')
# print(data)
train_x = data[["Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]]
# print(train_x)


# LabelEncoder 将性别转化为0，1
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train_x['Gender'] = le.fit_transform(train_x['Gender'])

kmeans = KMeans(n_clusters=3)
# 规范化到[0,1]空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
print(train_x)
# 使用kmeans进行聚类
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)

# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("customer_cluster_result.csv",index=False)
