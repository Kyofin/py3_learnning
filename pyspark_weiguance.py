# -*- coding: utf-8 -*-
from pyspark.sql import functions as fn
import pandas as pd
from pyspark.sql import SparkSession
import sys  # 要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')
'''
使用python2
pyspark去除或填充未观测数据
'''
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df_miss = spark.createDataFrame([
    (1, 143.5, 5.6, 28, 'M', 10000),
    (2, 167.2, 5.4, 45, 'M', None),
    (3, None, 5.2, None, None, None),
    (4, 144.5, 5.9, 33, 'M', None),
    (5, 133.2, 5.7, 54, 'F', None),
    (6, 124.1, 5.2, None, 'F', None),
    (7, 129.2, 5.3, 42, 'M', 76000)
], ['id', 'weight', 'height', 'age', 'gender', 'income'])

# 查找每行缺少的观测数据
# 可以观测到id=3的行有4个缺失数据
print df_miss.rdd.map(
    lambda row: (row['id'], sum([c == None for c in row]))
).collect()

# 检查每一列中缺失的观测数据百分比,
# 可以观测到：weight列和gender列屮缺失的14%观测数据是height列的两倍.并且儿乎是 income列缺失的观测数据的72%
df_miss.agg(
    *[
        (1-(fn.count(c) / fn.count('*'))).alias(c + '_missing')
        for c in df_miss.columns
    ]
).show()

# 移除'income'特征，因为它大部分值都是缺失的
df_miss_no_income = df_miss.select(
    [c for c in df_miss.columns if c != 'income']
)
# 不需要移除ID为3的行.因为这一行在‘weight’ 列和‘age’ 中有足够的现测数据来计算平均值并且填充缺失值的地方
df_miss_no_income.show()

# 只要超过三个null的行都移除
df_miss_no_income.dropna(thresh=3).show()

# 只要有null的行都移除
df_miss_no_income.dropna().show()

# 计算每列平均值，并转成字典
# 忽略gender列，因为算不出一个类别(性别)变量的平均数
means = df_miss_no_income.agg(
    *[
        fn.mean(c).alias(c)
        for c in df_miss_no_income.columns if c != 'gender'
    ]
).toPandas().to_dict('records')[0]
# 对字典增加gender：missing键值对
means['gender'] = 'missing'
print means

# 对缺失null值的地方按字典规则填充
df_miss_no_income.fillna(means).show()
