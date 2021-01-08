#!/usr/bin/env python3

"""
python3
爬取腾讯新闻新冠数据
"""
import json
import requests
from xpinyin import Pinyin
import datetime
import os
from hdfs.client import Client

pinyin = Pinyin()
hdfs_client = Client("http://10.93.6.7:50070/")



def get_province_feiyan_data(province):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=' + province

    r = requests.post(url, headers=headers)
    return r.text


def get_city_feiyan_data(province, city):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=' + province + "&city=" + city

    r = requests.post(url, headers=headers)
    return r.text


# 获取病人路途追踪
def get_patient_track_data():
    # request 请求
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    all_track_list = []
    page_index = 0
    while True:
        url = "https://pacaio.match.qq.com/virus/trackList?page=" + str(page_index) + "&num=1000"
        r = requests.get(url, headers=headers)
        one_page_track_list = json.loads(r.text)['data']['list']
        if len(one_page_track_list) == 0:
            break
        # 一页中所有元素追加到one_page_track_list
        all_track_list.extend(one_page_track_list)
        page_index += 1
    print("已获取病人路径" + str(len(all_track_list)) + "条数据")
    return all_track_list


# 根据省份获取城市名列表
def get_province_cities(province):
    # print("正在获取" + province + "的城市列表")
    province_pin_yin = pinyin.get_pinyin(province, '')
    # 修正重庆的拼音
    if province == "重庆":
        province_pin_yin = "chongqing"
    # 修正西藏的拼音
    if province == "西藏":
        province_pin_yin = "xizang"

    # request 请求
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    url = 'https://mat1.gtimg.com/news/feiyanarea/' + province_pin_yin + ".json"

    city_list = []
    r = requests.get(url, headers=headers)
    city_arr = json.loads(r.text)['features']
    for i in range(len(city_arr)):
        city_name = city_arr[i]['properties']['name']
        # 去除市
        city_name_alias = city_name
        if city_name.endswith("市"):
            city_name_alias = city_name[:-1]
        city_list.append({'province': province,
                          'province_pin_yin': province_pin_yin,
                          'city': city_name,
                          'city_name_alias': city_name_alias})
    # print(len(city_list))
    return city_list


# 获取国外新冠数据
def get_foreign_feiyan_data(country):
    url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=" + country
    r = requests.get(url)
    foreign_list = json.loads(r.text)['data']
    if foreign_list is None:
        return
    # 填充国家字段
    for i in range(len(foreign_list)):
        foreign_list[i]['country'] = country
    print("已获取" + country + "共" + str(len(foreign_list)) + "条数据")
    return foreign_list


def get_country_dict():
    url = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoforeignList"
    r = requests.get(url)
    foreign_list = json.loads(r.text)['data']['FAutoforeignList']
    return foreign_list


def callback(filename, size):
    print(filename, "完成了一个chunk上传", "当前大小:", size)
    if size == -1:
        print(filename+"文件上传完成")


if __name__ == '__main__':
    scheduler_time = datetime.datetime.now().strftime('%Y-%m-%d')
    output_path = "/Users/huzekang/study/py3_learnning/out/" + scheduler_time + "/"
    hdfs_path = "/data/feiyan"

    # 创建输出目录
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    print("调度时间：" + scheduler_time)
    # get_province_city("重庆")
    # 没有市区的省份字典
    provinces = ["北京",
                 "上海",
                 "天津",
                 "台湾",
                 "香港",
                 "澳门"]
    # 有市区的省份字典
    provinces2 = [
        "河北",
        "山西",
        "内蒙古",
        "辽宁",
        "吉林",
        "黑龙江",
        "江苏",
        "浙江",
        "安徽",
        "福建",
        "江西",
        "山东",
        "河南",
        "湖北",
        "湖南",
        "广东",
        "广西",
        "海南",
        "重庆",
        "四川",
        "贵州",
        "云南",
        "西藏",
        "陕西",
        "甘肃",
        "青海",
        "宁夏",
        "新疆"
    ]

    countries = get_country_dict()

    print("========== 开始爬取国外新冠肺炎数据 ==========")
    country_data_json_str_list = []
    for country in countries:
        country_data_list = get_foreign_feiyan_data(country['name'])
        for item in country_data_list:
            # 填充洲字段
            item['continent'] = country['continent']
            item_json_str = json.dumps(item, sort_keys=True, ensure_ascii=False)
            country_data_json_str_list.append(item_json_str)
    # 写出国外新冠数据
    file_object = open(output_path + 'foreign_feiyan_info.txt', 'w')
    file_object.writelines("\n".join(country_data_json_str_list))
    file_object.close()
    print("========== 结束爬取国外新冠肺炎数据 ==========")

    print("========== 开始爬取中国省份新冠肺炎数据 ==========")
    all_provinces = provinces + provinces2
    province_json_data = []
    for i in all_provinces:
        data = json.loads(get_province_feiyan_data(i))
        province_feiyan_data_list = data['data']
        print("已获取省份" + i + str(len(province_feiyan_data_list)) + "条数据")
        for o in province_feiyan_data_list:
            province_json_data.append(json.dumps(o, sort_keys=True, ensure_ascii=False))
    # 写省份肺炎数据文件
    file_object = open(output_path + 'province_feiyan_info.txt', 'w')
    file_object.writelines("\n".join(province_json_data))
    file_object.close()
    print("========== 结束爬取中国省份新冠肺炎数据 ==========")

    print("========== 开始爬取中国城市新冠肺炎数据 ==========")
    city_feiyan_data = []
    province_city_mapping_data = []
    for i in provinces2:
        cities = get_province_cities(i)
        for i in cities:
            # 记录省份和城市的映射关系
            province_city_mapping_data.append(json.dumps(i, sort_keys=True, ensure_ascii=False))
            # 获取城市肺炎的数据
            province_name = i['province']
            city_name_alias = i['city_name_alias']
            data = json.loads(get_city_feiyan_data(province_name, city_name_alias))
            city_feiyan_data_list = data['data']
            if city_feiyan_data_list is not None:
                print("已获取" + province_name + city_name_alias + str(len(city_feiyan_data_list)) + "条数据")
                for o in city_feiyan_data_list:
                    city_feiyan_data.append(json.dumps(o, sort_keys=True, ensure_ascii=False))
            else:
                print(province_name + "-" + city_name_alias + " 没有获取到新冠肺炎数据")
    # 写出城市肺炎数据文件
    file_object = open(output_path + 'city_feiyan_info.txt', 'w')
    file_object.writelines("\n".join(city_feiyan_data))
    file_object.close()
    # 写出城市身份映射关系文件
    file_object = open(output_path + 'province_city_mapping.txt', 'w')
    file_object.writelines("\n".join(province_city_mapping_data))
    file_object.close()
    print("========== 结束爬取中国城市新冠肺炎数据 ==========")

    print("========== 开始爬取新冠肺炎病人行径数据 ==========")
    track_list_data = get_patient_track_data()
    track_json_str_list = []
    for i in range(len(track_list_data)):
        track_json_str_list.append(json.dumps(track_list_data[i], sort_keys=True, ensure_ascii=False))
    # 写出新冠肺炎病人行径数据
    file_object = open(output_path + 'feiyan_track_info.txt', 'w')
    file_object.writelines("\n".join(track_json_str_list))
    file_object.close()
    print("========== 结束爬取新冠肺炎病人行径数据 ==========")

    print("========== 开始上传爬取数据到hdfs ==========")
    # 上传成功返回 hdfs_path
    hdfs_client.upload(hdfs_path=hdfs_path, local_path=output_path, chunk_size=2 << 19, progress=callback, cleanup=True)
    print("========== 结束上传爬取数据到hdfs ==========")
