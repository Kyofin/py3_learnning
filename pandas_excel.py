import pandas as pd

'''
    该函数主要的参数为io、sheetname、header、names、encoding。
    io:excel文件，可以是文件路径、文件网址、file-like对象、xlrd workbook;
    sheetname:返回指定的sheet，参数可以是字符串（sheet名）、整型（sheet索引）、list（元素为字符串和整型，返回字典{'key':'sheet'}）、none（返回字典，全部sheet）;
    header:指定数据表的表头，参数可以是int、list of ints，即为索引行数为表头;
    names:返回指定name的列，参数为array-like对象。
    encoding:关键字参数，指定以何种编码读取。
    该函数返回pandas中的DataFrame或dict of DataFrame对象，利用DataFrame的相关操作即可读取相应的数据。
'''
import pandas as pd
# 读excel
excel_path = '/System/Volumes/Data/Users/huzekang/Documents/朝阳医院2018年销售数据.xlsx'
df = pd.read_excel(excel_path, sheetname=None)
print(df)
# 写出excel 结果如图：![](https://i.loli.net/2019/11/28/KqhMWX8PTpURzJb.png)
writer = pd.ExcelWriter('output.xlsx')
df1 = pd.DataFrame(data={'col1': [1, 1], 'col2': [2, 2]})
df1.to_excel(writer, 'Sheet1')
writer.save()
