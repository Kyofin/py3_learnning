import pandas as pd

'''
python3 该示例展示将execl转csv
'''
import pandas as pd


def xlsx_to_csv_pd():
    data_xls = pd.read_excel('/Volumes/Samsung_T5/huzekang/dataset/企业信息数据.xlsx', index_col=0)
    data_xls.to_csv('/Volumes/Samsung_T5/huzekang/dataset/企业信息数据.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()
