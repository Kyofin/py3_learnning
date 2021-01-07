#!/usr/bin/env python3

"""
python3
爬取腾讯新闻新冠数据
"""
import json
import requests
from xpinyin import Pinyin

pinyin = Pinyin()


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


# 根据省份获取城市名列表
def get_province_city(province):
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
        if city_name.endswith("市"):
            city_name = city_name[:-1]
        city_list.append({'province': province, 'city': city_name})
    # print(len(city_list))
    return city_list


if __name__ == '__main__':
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

    print("========== 开始爬取中国省份新冠肺炎数据 ==========")
    all_provinces = provinces + provinces2
    province_json_data = []
    for i in all_provinces:
        data = json.loads(get_province_feiyan_data(i))
        for o in data['data']:
            province_json_data.append(json.dumps(o, sort_keys=True, ensure_ascii=False))
    # 写出文件
    file_object = open('province_feiyan_info.txt', 'w')
    file_object.writelines("\n".join(province_json_data))
    file_object.close()
    print("========== 结束爬取中国省份新冠肺炎数据 ==========")

    print("========== 爬取中国城市新冠肺炎数据 ==========")
    city_json_data = []
    for i in provinces2:
        citys = get_province_city(i)
        # print(citys)
        for i in citys:
            province_name = i['province']
            city_name = i['city']
            data = json.loads(get_city_feiyan_data(province_name, city_name))
            if data['data'] != None:
                for o in data['data']:
                    city_json_data.append(json.dumps(o, sort_keys=True, ensure_ascii=False))
            else:
                print(province_name+"-"+city_name+" 没有获取到新冠肺炎数据")
    # 写出文件
    file_object = open('city_feiyan_info.txt', 'w')
    file_object.writelines("\n".join(city_json_data))
    file_object.close()
