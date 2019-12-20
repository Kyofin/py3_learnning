# -*- coding: utf-8 -*- 
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys) 
sys.setdefaultencoding('utf-8') 
from pyspark.sql import SparkSession
import pandas as pd
'''
使用python2
'''
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.createDataFrame([
    (1,144.5,5.9,33,'M'),
    (2,167.2,5.4,45,'M'),
    (3,124.1,5.2,23,'F'),
    (4,144.5,5.9,33,'M'),
    (5,133.2,5.7,54,'F'),
    (3,124.1,5.2,23,'F'),
    (5,129.2,5.3,42,'M'),
],['id','weight','height','age','gender'])
# 展示数据
df.show()