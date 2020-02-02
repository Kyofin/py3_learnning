# -*- coding: utf-8 -*-
from pyspark.sql import functions as fn
import pandas as pd
from pyspark.sql import SparkSession
import sys  # 要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')
'''
使用python2
pyspark读取hive
hive必须开启metastore服务。
即：~/opt/hadoop-cdh/hive-1.1.0-cdh5.14.2 » bin/hive --service metastore -p 9083
'''
spark = SparkSession.builder.appName("hive").enableHiveSupport().getOrCreate()

spark.sql("show tables").show()


