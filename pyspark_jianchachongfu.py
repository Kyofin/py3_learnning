# -*- coding: utf-8 -*-
from pyspark.sql import functions as fn
import pandas as pd
from pyspark.sql import SparkSession
import sys  # 要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')
'''
使用python2
pyspark检查重复数据
'''
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.createDataFrame([
    (1, 144.5, 5.9, 33, 'M'),
    (2, 167.2, 5.4, 45, 'M'),
    (3, 124.1, 5.2, 23, 'F'),
    (4, 144.5, 5.9, 33, 'M'),
    (5, 133.2, 5.7, 54, 'F'),
    (3, 124.1, 5.2, 23, 'F'),
    (5, 129.2, 5.3, 42, 'M'),
], ['id', 'weight', 'height', 'age', 'gender'])
# 展示数据
df.show()

# 检查重复数据
print('count of rows: {0}'.format(df.count()))
print('count of distinct rows: {0}'.format(df.distinct().count()))
# 去除完全重复数据
df = df.dropDuplicates()
df.show()

# 检查除去id列的重复数据
cols = []
for c in df.columns:
    if c != 'id':
        cols.append(c)
print('count of rows: {0}'.format(df.count()))
print('count of distinct rows: {0}'.format(df.select(cols).distinct().count()))
# 去除除id外完全重复数据
df = df.dropDuplicates(subset=cols)
df.show()

# 计算id总数和id唯一数
df.agg(
    fn.count('id').alias('id_count'),
    fn.countDistinct('id').alias('id_distinct')
).show()

# 为每条记录提供唯一自增id
df.withColumn('new_id',fn.monotonically_increasing_id()).show()
