# coding utf-8

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# 按照客户分组
def get_products(data):
    products = data.groupby(data['客户ID'])['产品名称'].value_counts().unstack()
    products[products > 1] = 1
    products[np.isnan(products)] = 0
    return products

# 用apriori算法得到频繁项集和关联规则并打印
def get_rule(encoded_transaction, min_support=0.05, min_threshold=1):
    frequent_itemsets = apriori(encoded_transaction, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric='lift', min_threshold=min_threshold)

    frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
    print('频繁项集：', frequent_itemsets)

    pd.options.display.max_columns = 100
    rules = rules.sort_values(by='lift', ascending=False)
    print('关联规则：', rules)

    return frequent_itemsets, rules


def main():
    # 读入数据
    data = pd.read_csv('./订单表.csv', encoding='gbk')
    # 清洗数据
    products = get_products(data)
    # 用apriori算法得到频繁项集和关联规则并打印
    frequent_itemsets, rules = get_rule(products, min_support=0.05, min_threshold=1)


if __name__ == "__main__":
    main()